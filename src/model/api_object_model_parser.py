from textwrap import dedent

from langchain.output_parsers import PydanticOutputParser
from langchain.output_parsers.pydantic import T

class ApiCaseParser(PydanticOutputParser):

    def get_format_instructions(self) -> str:
         prompt = super().get_format_instructions()

         api_prompt = dedent(f"""
         以上是JSON接口文档,里面是真实的接口,请基于接口参数编写测试用例,
         背景：提升编写接口case的效率，
         要求：1.按照行业写接口的规则，所有接口、所有参数都需要校验。2.case不少于50条。3.按照传入的CaseModel里面的属性生成结构化case
         请编写接口的测试用例
         
        {prompt}
         """)
         return  api_prompt
