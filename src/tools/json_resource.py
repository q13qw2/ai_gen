
from langchain.document_loaders import JSONLoader

import json
from pathlib import Path
from pprint import pprint

class JSONLoader():
    def getJson(self):
        file_path='../resource/api.json'
        data = json.loads(Path(file_path).read_text())
        return data