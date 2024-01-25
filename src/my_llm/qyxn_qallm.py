from langchain.llms import ChatGLM

class GaoTu(ChatGLM):
    def __init__(self):
        endpoint_url = "http://test-aiproxy.baijia.com/openai"
        super(MyChatLLM, self).__init__(endpoint_url=endpoint_url, max_token=80000,
                                        history=[["你是一名互联网大佬", "欢迎问我任何问题。"]],
                                        top_p=0.9,
                                        model_kwargs={
    "input": [
        {
            "role": "user",
            "content": "如何评价 人工智能"
        }
    ],
    "model_type": "chat",
    "caller": "0056_test",
    "key": "112296cd5bf741338bbee9a796db8181",
    "prefer": "azure",
    "api_args": {
        "stream": false,
        "max_tokens": 2000
    },
    "max_length": 2048,
    "n_try": 1,
    "retry_sleep": 1,
    "timeout": 60,
    "request_id": "0056"
})
