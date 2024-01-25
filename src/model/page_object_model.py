from pydantic import BaseModel,Field
from .element_model import ElementModel
from .method_model import MethodModel


# 间接生成一个PO模型，按照我的大概定义，生成之后我们在转换为一个Python代码
class PageObjectModel(BaseModel):

    '''
    直接生成数据
    比直接生成代码的好处是可以人工维护
    '''
    # 为了让大模型更理解我们的参数，所以需要加一些注释，通过Field
    elements: list[ElementModel] = Field(description="elements是存放所有的关键页面元素的列表，是一个列表，每个元素都有selector和name组成")
    method: list[MethodModel] = Field(description="methods是存放所有的关键方法的列表，每个方法有name、parameters、steps和return_type组成")

    def generate_source(self):
        ...
        """
        根据PageObjectModel的内容生成源代码,使用jinja模板引擎生成python代码
        ：return
        """
        # 根据PageObjectModel的内容生成源代码,使用jinja模板引擎生成python代码，请在下一行补充代码
        pass