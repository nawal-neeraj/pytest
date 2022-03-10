from pydantic import BaseModel

class AddValues(BaseModel):
    value_one = int
    value_two = int