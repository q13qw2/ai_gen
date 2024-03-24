from src.my_llm.open_ai import MyOpenAI
from langchain.agents import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.tools.convert_to_openai import format_tool_to_openai_function
from langchain.agents import AgentExecutor

@tool
def get_word_length(word: str) -> int:
    """返回一个单词的长度。"""
    return len(word)

def test_custom_agent():
    llm = MyOpenAI()

    tools = [get_word_length]

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are very powerful assistant, but don't know current events"),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ]
    )

    llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

    from langchain.agents.format_scratchpad import format_to_openai_function_messages
    from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser

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
    agent_executor.invoke({"input": "单词counterattack有多少个字母？"})

