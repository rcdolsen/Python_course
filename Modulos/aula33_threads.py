# (Parte 1) Threads - Executando processamentos em paralelo

from threading import Lock, Thread
from time import sleep

"""
class MyThread(Thread):
    def __init__(self, texto, tempo):
        self.texto = texto
        self.tempo = tempo

        super().__init__()

    def run(self):
        sleep(self.tempo)
        print(self.texto)


t1 = MyThread('thread 1', 5)
t1.start()

t2 = MyThread('thread 2', 1)
t2.start()

t3 = MyThread('thread 3', 8)
t3.start()

for i in range(11):
    print(i)
    sleep(1)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Hello world 1', 3))
t2 = Thread(target=vai_demorar, args=('Hello world 2', 0))
t3 = Thread(target=vai_demorar, args=('Hello world 3', 8))

t1.start()
t2.start()
t3.start()

for i in range(10):
    print(i)
    sleep(.5)
"""

"""
def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Hello world 1', 10))
t1.start()
# t1.join()

while t1.is_alive():
    print('Loading')
    sleep(2)

print('the end')
"""


class Ingressos:
    """
    Classe que vende ingressos
    """

    def __init__(self, estoque) -> None:
        """ Inicializando...

        :param estoque: quantidade de ingressos em estoque
        """
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade: int):
        """
        Compra determinada quantidade de ingressos

        :param quantidade: A quantidade de ingressos que deseja comprar
        :type quantidade: int
        :return: Nada
        :rtype: None
        """
        # Tranca o método
        self.lock.acquire()

        if self.estoque < quantidade:
            print(f'nao ha ingressos suficientes. \n'
                  f'Ingressos restantes: {self.estoque}')
            print('')

            sleep(1)

            # Libera o método
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Voce comprou {quantidade} ingresso(s). \n'
              f'Ingressos restantes: {self.estoque}')
        print('')

        # Libera o método
        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)

    for i in range(1, 15):
        t = Thread(target=ingressos.comprar, args=(1,))
        t.start()
