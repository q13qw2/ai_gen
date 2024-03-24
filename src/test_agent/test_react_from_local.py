from langchain.agents import  initialize_agent,load_tools,AgentType
from langchain.prompts import ChatPromptTemplate
from src.my_llm.open_ai import MyOpenAI
from langchain.globals import set_debug, set_verbose
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from src.tools.local_data_base_search import LocalDatabaseSearch

# set_debug(True)
# set_verbose(True)
def test_react_local():

    chat_model = MyOpenAI()

    tools = load_tools(["llm-math"], llm=chat_model)
    # 实例化你的本地数据库搜索工具
    local_search_tool = LocalDatabaseSearch(host='localhost',
                                            user='root',
                                            password='5211314321',
                                            database='agent')

    # 使用这个工具进行查询
    result = local_search_tool.run("姚明")
    print(result)

    # 检查查询结果，如果查询成功且含有所需信息，则继续
    if "配偶" in result and "年龄差" in result:
        # 初始化 Agents
        agent = initialize_agent(tools, chat_model, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True,
                                 handle_parsing_errors=True)

        # 构造一个更具体的查询，以获取更详细的信息
        # detailed_query = f"姚明的妻子是{result['配偶']}。她的年龄差是{result['年龄差']}岁。他们年龄差的2次方是多少？"
        detailed_query = f"已知姚明的妻子是{result['配偶']}，他们的年龄差是{result['年龄差']}岁。请计算这个年龄差的2次方值。"

        # 测试一下！
        agent.run(detailed_query)
    else:
        print(result.get("error", "查询失败"))