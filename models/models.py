from pydantic import BaseModel

class add_values(BaseModel):
    value_one = int
    value_two = int