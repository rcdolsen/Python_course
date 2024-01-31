from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, agency: int, account: int, balance) -> None:
        self.agency = agency
        self.account = account
        self.balance = balance

    @abstractmethod
    def withdraw(self, valor: float) -> float:
        ...

    def deposit(self, value: float) -> float:
        self.balance += value
        self.detail(f'($ {value}) depositado com sucesso')
        return self.balance

    def detail(self, msg: str = '') -> None:
        print(f'{msg}. O seu saldo disponivel e: $ {self.balance:.2f}')

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'(Agency: {self.agency}, account: {self.account},'\
            f'balance: {self.balance})'
        return f'{class_name}, {attrs}'


class SavingsAccount(Account):
    def __init__(self, agency: int, account: int, balance: float = 0):
        super().__init__(agency, account, balance)
        self._balance = balance

    def withdraw(self, value: float) -> float:
        if value <= self._balance:
            self._balance -= value
            self.detail(f'({value}), sacado com sucesso')
            return self._balance

        self.detail(f'valor de saque({value}) maior que o disponivel')
        return self._balance


class CurrentAccount(Account):
    def __init__(self, agency: int, account: int, balance: float = 0, limit=0):
        super().__init__(agency, account, balance)
        self._balance = balance
        self._limit = limit

        if __name__ == '__main__':
            print(f'O limite da conta e $ {self._limit:.2f}')
            print('')

    def withdraw(self, value: float) -> float:
        if value <= self._balance + self._limit:
            self._balance -= value
            self.detail(f'{value}, sacado com sucesso')
            return self._balance
        else:
            self.detail(f'valor de saque({value}) maior que o disponivel')
            print('O saque maximo disponivel e:$ '
                  f'{self._balance + self._limit:.2f}')
            return self._balance

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'(agency: {self.agency}, account: {self.account},'\
            f' balance: {self._balance}, limit: {self._limit})'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':

    print('-' * 20, 'poupanca', '-' * 20)
    savings = SavingsAccount(111, 222)
    savings.deposit(10)
    savings.deposit(10)
    savings.withdraw(30)
    savings.deposit(50)
    savings.withdraw(30)

    print('-' * 20, 'corrente', '-' * 20)

    current = CurrentAccount(111, 222, 0, 100)
    current.deposit(10)
    current.deposit(10)
    current.withdraw(30)
    current.deposit(50)
    current.withdraw(300)
