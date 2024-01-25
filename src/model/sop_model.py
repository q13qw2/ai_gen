from pydantic import BaseModel,Field
from .page_object_model import PageObjectModel
from .method_model import MethodModel
class SPOModel(BaseModel):
    """
    代表两个page object model的跳转关系
    """
    source : PageObjectModel = Field(description="源页面的page object model对象结构")
    target : PageObjectModel = Field(description="目标页面的page object model对象结构")
    method : MethodModel = Field(description="跳转的方法,比如login，代表登录")