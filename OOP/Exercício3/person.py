import accounts


class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self.name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self.age = age

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.name!r}, {self.age!r})'
        return f'{class_name}, {attrs}'


class Client(Person):
    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)
        self.account: accounts.Account | None = None


if __name__ == '__main__':

    c1 = Client('Marrom', 5)
    c1.account = accounts.SavingsAccount(111, 222, 0)
    c1.account.withdraw(20)
    print(c1)
    print(c1.account)

    print('')

    c2 = Client('Theo', 0)
    c2.account = accounts.CurrentAccount(111, 223, 0, 100)
    c2.account.deposit(50)
    print(c2)
    print(c2.account)
