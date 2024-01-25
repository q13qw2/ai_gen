from pydantic import BaseModel,Field

class SetModel(BaseModel):
    """
    代表单个步骤的基本信息，里面包含了步骤的操作和数据
    """
    action : str = Field(description="操作，比如click，send_keys")
    target: str = Field(description="操作的目标，比如登录按钮，用户输入框，手机验证码输入框，下拉框，也可以是一个name，与ElementModel的name对应")
    description: str = Field(description="步骤的描述，比如点击登录按钮")