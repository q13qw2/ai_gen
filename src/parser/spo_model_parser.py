from textwrap import dedent

from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers.pydantic import T

class SPOModelParser(PydanticOutputParser):

    def get_format_instructions(self) -> str:
        prompt = super().get_format_instructions()

        #todo 把每个对象模型的字段丰富到这里，比如element是啥
        prompt = super().get_format_instructions()
        po_prompt = dedent(f"""
            请根据上述对话，创建一个JSON结构，代表自动化测试的SPO类，JSON结构参考SPOModel的定义
            {prompt}
        """)

        return  po_prompt