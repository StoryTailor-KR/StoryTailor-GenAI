from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import List, Dict
from langchain_core.pydantic_v1 import BaseModel, Field

chat_llm = ChatOpenAI(model_name="gpt-4-0125-preview")

prompt_template="""
You're prompt engineer who make prompt for Image Generative AI.

[Rule]
- prompt should be English.
- Each paragraph in the story turns into its own prompt.
- The end of the prompt should always end with 'cartoon style. color pencil sketch.'
- The prompt should describe the story as if depicting a scene, using just 2 or 3 concise sentences.
- Describe the attributes of the subject, not its name. Example : When depicting a puppy named 'Choco', describe a puppy instead of 'Choco'.
- Avoid using phrases unrelated to the scene, such as 'A once upon a time' or 'One day.'

YOU MUST MAKE RESPONSE LIST TYPE.
output example:
["prompt1", "prompt2", "prompt3", "prompt4"]

[Example]
story : 철수는 스케이트보드로 킥플립 연습을 열심히 하고있어요.
-> Let's depict it as a scene.
-> scene : a man is doing a kickflip.
-> make prompt in cartoon style. color pencil sketch.
--> prompt : a man is doing a kickflip. cartoon style. color pencil sketch.
story : 로봇은 많은 연습 끝에 거대한 파도를 서핑할 수 있게 되었어요. 로봇의 제일 좋아하는 꽃무늬 셔츠를 입은채로 말이죠.
-> Let's depict it as a scene.
-> scene : a robot wearing a flower shirt surfing a huge wave.
-> make prompt in cartoon style. color pencil sketch.
--> prompt : a robot wearing a flower shirt surfing a huge wave. cartoon style. color pencil sketch.


story : {user_input}
"""

PROMPT = PromptTemplate(
    template=prompt_template, input_variables=["user_input"]
)

class imgPrompt(BaseModel):
    imgPrompt: List[str] = Field(description="이미지 프롬프트")

parser = JsonOutputParser(pydantic_object=imgPrompt)

async def imgPrompt_chain():
    return PROMPT | chat_llm | parser