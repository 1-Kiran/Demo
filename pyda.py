from pydantic import BaseModel,Field

class Students(BaseModel):
    id: int
    name: str
    age:int = Field(ge=18,le=30)
    sal: float