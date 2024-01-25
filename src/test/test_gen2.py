from langchain.prompts import ChatPromptTemplate
from src.tools.llm_factory import LLMFactry
from src.tools.html_resource import HTMLResource

def test_gen():

    # web_html = (Path().parent / 'web.html').read_text(encoding='utf-8')
    web_html = HTMLResource().get_web_resouce()
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful AI bot. Your name is {name}."),
            ("human", "{web_html}"),
            ("human", "{query}"),
        ]
    )
    url = 'https://aiproxy.baijia.com/proxy/openai/v1'
    key = '7ee7c1d345a94404bbdfaf1392ae4db5'
    chat_llm = ChatOpenAI(base_url=url,temperature=0.0, api_key=key,model='gpt-3.5-turbo')
    # chat_llm = LLMFactry().get_llm('openai')

    chain = chat_template | chat_llm
    output = chain.invoke({
        'name':'宋兆军',
        'query':'以上是一段html代码，代表了某个网页。基于上述代码，请创建一个自动化测试的Page Object类',
        'web_html':web_html
    })

    print(output)

if __name__ == '__main__':
    test_gen()