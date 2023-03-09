from typing import List

from pydantic import BaseModel, ValidationError


class Address(BaseModel):
    street: str
    building: int


class Person(BaseModel):
    age: int
    name: str
    is_married: bool
    address: Address
    languages: List[str]


data = {
    "age": 10,
    "name": "John",
    "is_married": False,
    "address": {"street": "st street", "building": 10},
    "languages": ["pt-pt", "en-us"],
}

try:
    person = Person(**data)
    print(person.dict())
except ValidationError as e:
    errors = e.errors()
    for error in errors:
        print(error["loc"])
        print(error["msg"])
        print(error["type"])
    print(e.json())
