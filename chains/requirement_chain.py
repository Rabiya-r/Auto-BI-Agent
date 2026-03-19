from langchain_core.output_parsers import PydanticOutputParser
from models.requirement_model import Requirement
from prompts.requirement_prompt import requirement_prompt
from utils.llm import llm

parser = PydanticOutputParser(pydantic_object=Requirement)

requirement_chain = requirement_prompt | llm | parser