from gc import set_debug
from pathlib import Path
from src.model.sop_model import SPOModel
from src.parser.spo_model_parser import SPOModelParser
import yaml
from langchain.prompts import ChatPromptTemplate
from src.model.api_object_model_parser import ApiCaseParser
from src.model.case_model import CaseModel
from src.tools.json_resource import JSONLoader
from src.tools.llm_factory import LLMFactry

set_debug(True)
def test_gen6():
    from pathlib import Path

    # pre = (Path(__file__).parent / 'src' / 'resource' / 'pre.html').read_text(encoding='utf-8')
    # next = (Path(__file__).parent / 'src' / 'resource' / 'next.html').read_text(encoding='utf-8')
    pre_file_path = Path('/Users/mac/Documents/myWorld/ai_gen/src/resource/pre.html')
    pre = pre_file_path.read_text(encoding='utf-8')
    next_file_path = Path('/Users/mac/Documents/myWorld/ai_gen/src/resource/next.html')
    next = next_file_path.read_text(encoding='utf-8')

    chat_llm = LLMFactry().get_llm("openai")

    parser = SPOModelParser(pydantic_object=SPOModel)

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "你是一名专业的测试专家，你精通于测试自动化测试，精通于数据驱动测试，精通于接口测试，精通于UI测试."),
            ("human", "当前页面为 {pre}"),
            ("human", "经过步骤 {method} 进入下一个页面"),
            ("human", "下一个页面为 {next}"),
            ("human", "{format_instructions}"),
        ]
    )

    chain = chat_template | chat_llm

    output = chain.invoke({
        'pre':pre,
        'method':'发送验证码，验证码111111，点击登录按钮',
        'next':next,
        'format_instructions': parser.get_format_instructions()
    })

    debug(output.content)
    r=parser.parse(output.content)
    print(r.__class__)
    debug(r)

if __name__ == '__main__':
    test_gen6()