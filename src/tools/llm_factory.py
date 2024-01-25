
from src.my_llm.my_chatllm import MyChatLLM
from langchain_community.chat_models import ChatOpenAI

class LLMFactry():
    def get_llm(self,name):
        if name == 'chatglm':
            return MyChatLLM()
        elif name == 'openai':
            url = 'https://aiproxy.baijia.com/proxy/openai/v1'
            key = '7ee7c1d345a94404bbdfaf1392ae4db5'
            return ChatOpenAI(model='gpt-3.5-turbo-16k', base_url=url, temperature=0.0, openai_api_key=key,max_tokens=16000)