
from langchain.document_loaders import UnstructuredHTMLLoader

class HTMLResource:
    def get_web_resouce(self):
        loader = UnstructuredHTMLLoader("../resource/web.html")
        data = loader.load()
        return data