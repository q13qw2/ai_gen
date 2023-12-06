
from src.my_llm.my_chatllm import MyChatLLM
from langchain.llms.openai import OpenAI


class LLMFactry:
    def get_llm(self,name):
        if name == 'chatglm':
            return MyChatLLM()
        elif name == 'openai':
            return OpenAI()