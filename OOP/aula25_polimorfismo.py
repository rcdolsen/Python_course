# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação.
# Sobrecarga de métodos (overload)  🐍 = ❌
# Sobreposição de métodos (override) 🐍 = ✅
from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, msg) -> None:
        self.msg = msg

    @abstractmethod
    def enviar(self) -> bool: ...

class Email(Notificacao):
    def enviar(self) -> bool:
        print('Enviando email:', self.msg)
        return True

class Sms(Notificacao):
    def enviar(self) -> bool:
        print('Enviando SMS:', self.msg)
        return True

def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao enviada')
    else:
        print('Notificacao nao enviada')

#send = Email('Notificacao')
#send.enviar()
notificacao_email = Email('Testando: email')
notificar(notificacao_email)

#send = Sms('Notificacao')
#send.enviar()
notificacao_sms = Sms('Testando: SMS')
notificar(notificacao_sms)
