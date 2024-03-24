from langchain.agents import  initialize_agent,load_tools,AgentType
from langchain.prompts import ChatPromptTemplate
from src.my_llm.open_ai import MyOpenAI
from langchain.globals import set_debug, set_verbose
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from src.tools.local_data_base_search import LocalDatabaseSearch

set_debug(True)
set_verbose(True)
def test_react():

    chat_model = MyOpenAI()

    # 记载几个工具，google的搜索，一个是数学计算的工具
    tools = load_tools(["serpapi", "llm-math"], llm=chat_model, serpapi_api_key="20c97317bec87ebea9061ca0833e627bd4149a70d5a2d6d7f59525ad4b3c9eb2")

    #  初始化一个agent,要有工具包，模型，agent类型（零样本的，基于react的提示词）
    agent = initialize_agent(
        tools,chat_model,agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,verbose=True,handle_parsing_errors=True
    )

    agent.run(
        "Who is Leonardo DiCaprio girlfriend? What is her current age raised to the 0.43 power?"
    )




