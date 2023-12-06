from gc import set_debug
from pathlib import Path

import yaml

from src.my_llm.my_chatllm import MyChatLLM
from langchain.prompts import ChatPromptTemplate
from src.model.api_object_model_parser import ApiCaseParser
from src.model.case_model import CaseModel
from src.tools.json_resource import JSONLoader
from src.tools.llm_factory import LLMFactry

set_debug(True)
def test_gen4():

    api_files = JSONLoader().getJson()

    print(api_files)
    print("看能否查询到内容：")
    chat_llm = LLMFactry().get_llm("chatglm")

    parser = ApiCaseParser(pydantic_object=CaseModel)

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "{api_files}"),
            ("human", "{format_instructions}"),
        ]
    )

    chain = chat_template | chat_llm

    output = chain.invoke({
        'name':'宋兆军',
        # 'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类(Java)',
        'api_files':api_files,
        'format_instructions': parser.get_format_instructions()
    })

    r=parser.parse(output)
    print(r.__class__)
    print(r)

if __name__ == '__main__':
    test_gen4()