# LangChain相关模块的导入
from src.my_llm.open_ai import MyOpenAI
from langchain.agents import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents import AgentExecutor
from src.tools.local_data_base_search import LocalDatabaseSearch
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# 确保已下载NLTK数据
nltk.data.path.append('/Users/mac/Documents/myWorld/Repos/nltk_data')
nltk.download('punkt', download_dir='/Users/mac/Documents/myWorld/Repos/nltk_data')
nltk.download('stopwords', download_dir='/Users/mac/Documents/myWorld/Repos/nltk_data')
nltk.download('wordnet', download_dir='/Users/mac/Documents/myWorld/Repos/nltk_data')

def determine_query_type(user_input):
    # 确保输入是字符串
    query_text = user_input['input']  # 提取实际的查询文本

    # 分词
    tokens = word_tokenize(query_text.lower())

    # 去除停用词并进行词形还原
    stop_words = set(stopwords.words('english'))
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stop_words]

    # 定义关键词
    age_difference_keywords = ["age difference", "years apart", "差几岁"]
    age_keywords = ["age", "岁数", "几岁", "芳龄"]

    # 检查是否命中关键词
    query_type = "spouse_name"  # 默认查询类型
    for token in lemmatized_tokens:
        if token in age_difference_keywords:
            query_type = "age_difference"
            break
        elif token in age_keywords:
            query_type = "age"
            break

    return query_type

llm = MyOpenAI()

@tool
def local_database_search(query: str,type : str) -> {}:
    # 方法名作为自定义tool的实例名称
    # query参数是经过大模型分析之后，送入当前tool的文本信息
    # 方法中必须要存在doc,这个doc会被作为tool的描述信息，提交给大模型用于判断什么时候怎么调用当前tool
    """接收中文文本，返回数据库中name对应的配偶信息是谁，查询对应的出生日期，计算两者之间的时间差，必须要接收一个中文文本作为输入参数，并且返回的时候总是一个字典数据，对应Key1为配偶信息，key2为年龄差"""

    # 实例化你的本地数据库搜索工具
    local_search_tool = LocalDatabaseSearch(host='localhost',
                                            user='root',
                                            password='123321',
                                            database='agent')
    return local_search_tool.run(query,type)

def test():
    llm = MyOpenAI()

    tools = [local_database_search]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are very powerful assistant, but don't know current events"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

    agent = (
            {
                "input": lambda x: x["input"],
                "agent_scratchpad": lambda x: format_to_openai_function_messages(x["intermediate_steps"]),
            }
            | prompt
            | llm_with_tools
            | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


    str = {"input": "姚明的老婆是谁？他们相差几岁？"}
    # 分析输入文本，调用agent执行
    query_type = determine_query_type(str)


    # 用户的原始输入
    user_input = "姚明的老婆是谁？他们相差几岁？"
    query_type = determine_query_type(user_input)

    # 调用LangChain的工作流，传入名字和查询类型
    # 注意：这里假设工具函数local_database_search和工作流支持传入query_type
    # 实际实现时可能需要调整LangChain工作流的绑定和调用方式以支持额外的参数

    agent_executor.invoke({"input": user_input, "type": query_type})
    # agent_executor.invoke({"input": "姚明的老婆是谁？他老婆年龄的平方是多少？请一步一步分析，不是年龄差的平方"})
    # agent_executor.invoke({"input": "姚明的老婆是谁？他们相差几岁？"})