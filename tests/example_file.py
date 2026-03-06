import typing

import pydantic


@typing.final
class ExampleModel(pydantic.BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True
