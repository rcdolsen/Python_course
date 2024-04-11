from collections.abc import Callable
from typing import TypeVar

a_string: str = "A value"
an_integer: int = 123
a_float: float = 1.23
a_boolean: bool = True
a_set: set = {1, 2, 3}
a_list: list = [1, 2, 3]
a_tuple: tuple = 1, 2, 3
a_dictionary: dict = {"name": "marrom"}


def som(x: int, y: int, z: float) -> float:
    return x + y + z


lint_int: list[int] = [1, 2, 3, 4]
lint_str: list[str] = ["a", "b", "c"]
lint_tuple: list[tuple] = [(1, "a"), (2, "b")]
lint_lists_int: list[list[int]] = [[1, 2], [3]]

a_dict: dict[str, list[int]] = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [1, 4],
}

a_set_int: set[int] = {1, 2, 3}

ListInt = list[int]
dictlistint = dict[str, ListInt]

a_dict_of_lists = dictlistint = {
    "A": [1, 2],
    "B": [3, 4],
    "C": [1, 4],
}

str_and_int: str | int = 1
str_and_int = "A"
str_and_int = 1
list_str_and_int: list[str | int] = [1, 2, 3, "a"]


def sum2(x: int, y: float | None = None) -> float:
    if isinstance(y, float | int):
        return x + y
    return x


print(sum2(1))
print(sum2(1, 2.1))
print(sum2(1, None))

call = Callable[[int, int], int]


def execute(func: call, a: int, b: int) -> int:
    return func(a, b)


#  dinamic typing
T = TypeVar("T")


def get_item(list: list[T], index: int) -> T:
    return list[index]


list_int = get_item([1, 2, 3], 1)
list_int = get_item(["a", "b", "c"], 1)


class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"


def say_my_name(person: Person) -> str:
    return person.full_name


def say_my_name_again(person: Person) -> list[Person]:
    return [person.lastname, person.firstname]


print(say_my_name_again(Person("Marrom", "Theo")))
print(say_my_name(Person("Marrom", "Theo")))
