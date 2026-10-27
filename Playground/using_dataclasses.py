import dataclasses
from dataclasses import dataclass

@dataclass
class Person:
    age: int
    height: float
    favorite_color: str

person = Person(age=25, height=5.9, favorite_color='blue')

for field in dataclasses.fields(person):
    value = getattr(person, field.name)
    field_name = field.name.replace("_", " ").title()

    print(f"{field_name}: {value} | Type: {type(value)}")
