import yaml

from langchain.prompts import ChatPromptTemplate
from src.model.page_object_model import PageObjectModel
from src.model.page_object_model_parser import PageObjectModelParser
from src.tools.html_resource import HTMLResource
from src.tools.llm_factory import LLMFactry

def test_gen3():

    # web_html = (Path().parent / 'web.html').read_text(encoding='utf-8')
    web_html = HTMLResource().get_web_resouce()
    chat_llm = LLMFactry().get_llm("chatglm")

    # parser = PydanticOutputParser(pydantic_object=PageObjectModel)
    parser = PageObjectModelParser(pydantic_object=PageObjectModel)

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "{web_html}"),
            # ("human", "{query} {format_instructions}"),
            ("human", "{format_instructions}"),
        ]
    )

    chain = chat_template | chat_llm

    output = chain.invoke({
        'name':'宋兆军',
        # 'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类(Java)',
        'web_html':web_html,
        'format_instructions': parser.get_format_instructions()
    })


    r=parser.parse(output)

    with open('po4.yaml','w') as f:
        yaml.dump(r,f,allow_unicode=True)

if __name__ == '__main__':
    test_gen3()