from pydantic import BaseModel,Field


# 输出：最终帮我生成这个对象  直接帮我生成代码
class CaseModel(BaseModel):
    '''
    解析大模型提供的代码
    利用元编程反向解析代码中的所有类、方法、参数和属性、反向保存为page model数据
    '''
    id: str = Field(description="用例编号，格式举例:Case_001")
    name: str = Field(description="用例名称，用一句话说明这条用例是做什么的")
    uri : str = Field(description="具体的接口")
    method : str = Field(description="接口的请求类型，GET/POST")
    paramers : str = Field(description="接口请求参数")
    api_result : str = Field(description="接口预期的返回结果")

