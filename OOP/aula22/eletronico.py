from log import LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if not self._ligado:
            self._ligado = True
        else:
            self.log_error(f'{self._nome} ja esta ligado')

    def desligar(self):
        if self._ligado:
            self._ligado = False
            print(f'{self._nome} ligado')
        else:
            self.log_error(f'{self._nome} ja esta desligado')

class Smartphone(Eletronico, LogFileMixin):
    def ligar(self):
        super().ligar()

        if self._ligado:
            msg = f'{self._nome} ligado'
            self.log_success(msg)
             
    def desligar(self):
        super().desligar()

        if not self._ligado:
            msg = f'{self._nome} desligado'
            self.log_success(msg)