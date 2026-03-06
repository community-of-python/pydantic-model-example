import pydantic


class ExampleModel(pydantic.BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True
