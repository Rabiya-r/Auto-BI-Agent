from chains.requirement_chain import requirement_chain
from utils.validators import validate_requirement

def requirement_agent(query: str):
    try:
        result = requirement_chain.invoke({
            "query": query,
            "format_instructions": requirement_chain.steps[-1].get_format_instructions()
        })

        result = validate_requirement(result)

        return result.dict()

    except Exception as e:
        print("Error:", e)
        return None