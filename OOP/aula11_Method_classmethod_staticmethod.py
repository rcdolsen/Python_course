# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        # Setter
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def login(msg):
        return msg
    
@staticmethod
def logout(msg):
    return msg

c1 = Connection()
print(c1.user)

print('1', '-' * 50)

c1 = Connection()
c1.set_user('Marrom')
print(c1.user)

print('2', '-' * 50)

c1.set_password('123')
print(c1.password)

print('3', '-' * 50)

c2 = Connection.create_with_auth('Marrom', '1234')
print(c2.user)
print(c2.password)

print('4', '-' * 50)

print(Connection.login('esta logado'))

print(logout('esta deslogado'))