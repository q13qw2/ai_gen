from pydantic import BaseModel

# 输出：最终帮我生成这个对象  直接帮我生成代码
class CodeModel(BaseModel):
    '''
    解析大模型提供的代码
    利用元编程反向解析代码中的所有类、方法、参数和属性、反向保存为page model数据
    '''
    code: str = None
    language: str = None
