from pydantic import BaseModel
from urllib.parse import urlencode

def model_to_query_string(model: BaseModel) -> str:
    model_to_dict = model.dict(exclude_none=True)

    query_string = urlencode(model_to_dict)

    return query_string