import accounts
import person


class Bank:
    def __init__(
            self,
            bank_agencies: list[int] | None = None,
            bank_accounts: list[accounts.Account] | None = None,
            bank_clients:  list[person.Person] | None = None,
    ):
        self.agencies = bank_agencies or []
        self.accounts = bank_accounts or []
        self.clients = bank_clients or []

    def _check_agency(self, account):
        if account.agency in self.agencies:
            print('agencia validada')
            return True
        print('agencia invalida')
        return False

    def _check_account(self, account):
        if account in self.accounts:
            print('conta validada')
            return True
        print('conta invalida')
        return False

    def _check_client(self, client):
        if client in self.clients:
            print('cliente validado')
            return True
        print('cliente invalido')
        return False

    def _check_if_account_is_client(self, client, account):
        if account is client.account:
            print('A conta e do cliente')
            print('operacao validada')
            return True
        print('A conta nao e do cliente')
        print('operacao nao validada')
        return False

    def authenticator(self, client: person.Person, account: accounts.Account):
        if self._check_agency(account) and \
                self._check_account(account) and \
                self._check_client(client) and \
                self._check_if_account_is_client(client, account):
            return True
        return False

    def __repr__(self) -> str:
        class_name = type(self).__name__
        attrs = f'({self.clients}\n\n{self.agencies}\n\n'\
            f'{self.accounts})'
        return f'{class_name}{attrs}'


marrom = person.Client('Marrom', 5)
marrom.account = accounts.CurrentAccount(111, 321, 0, 100)

theo = person.Client('Theo', 0)
theo.account = accounts.SavingsAccount(222, 3220, 0)

muzuda = person.Client('Muzuda', 35)
muzuda.account = accounts.CurrentAccount(15432, 154, 1000, 100)

bank = Bank()
bank.agencies.extend([111, 222, 333, 444, 555])
bank.clients.extend([marrom, theo, muzuda])
bank.accounts.extend([marrom.account, theo.account, muzuda.account])

if __name__ == '__main__':
    print(f'Cliente {marrom.name}')
    print('')
    bank.authenticator(marrom, marrom.account)

    print('-' * 50)
    print(f'Cliente {theo.name}')
    print('')
    bank.authenticator(theo, theo.account)

    print('-' * 50)
    print(f'Cliente {muzuda.name}')
    print('')
    bank.authenticator(muzuda, muzuda.account)

    print('-' * 50)
    bank.authenticator(theo, marrom.account)
