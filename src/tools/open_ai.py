# from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
class MyOpenAI(ChatOpenAI):
    def __init__(self):
        url = 'https://aiproxy.baijia.com/proxy/openai/v1'
        key = '7ee7c1d345a94404bbdfaf1392ae4db5'
        super(MyOpenAI, self).__init__(model='gpt-3.5-turbo', base_url=url, temperature=0.0, openai_api_key=key)