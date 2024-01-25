from pydantic import BaseModel,Field

class MethodModel(BaseModel):

    """
    代表单个方法的基本信息，里面包含了方法的名字、参数、步骤和返回值
    """
    name: str = Field(description="方法名，代表了这个方法的业务含义，比如login，代表登录")
    parameters: str = Field(description="方法的参数，比如用户名和密码")
    steps: str = Field(description="方法的步骤，比如点击登录按钮")
    return_type: str = Field(description="方法的返回值类型，比如登录成功后返回一个User对象，或者其他的Page Object对象")
