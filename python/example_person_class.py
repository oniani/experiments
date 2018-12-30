"""
Properties in Python
"""


class Person:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str):
        self._name = new_name

    name = property(get_name, set_name)

    def get_age(self) -> int:
        return self._age

    def set_age(self, new_age: int):
        self._age = new_age

    age = property(get_age, set_age)

    def __str__(self):
        return f"Person: {self._name}, {self._age} years old"


def main():
    person = Person("Homer Simpson", 39)
    print(person)

    person.name = "Donald Duck"
    person.age = 99999

    print(person)


if __name__ == "__main__":
    main()
