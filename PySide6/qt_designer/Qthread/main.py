import sys
import time

from PySide6.QtCore import QObject, QThread, Signal
from PySide6.QtWidgets import QApplication, QWidget

from worker import Ui_Form


class Worker1(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def run(self):
        value = '0'
        self.started.emit(value)
        for i in range(5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(1)
        self.finished.emit(value)


class Worker2(QObject):
    started = Signal(str)
    progressed = Signal(str)
    finished = Signal(str)

    def executeMe(self):
        value = '0'
        self.started.emit(value)
        for i in range(50, 1000, 5):
            value = str(i)
            self.progressed.emit(value)
            time.sleep(0.1)
        self.finished.emit(value)


class MyWidget(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.b1.clicked.connect(self.hardWork1)
        self.b2.clicked.connect(self.hardWork2)

    def hardWork1(self):
        self._worker1 = Worker1()
        self._thread1 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker1
        thread = self._thread1

        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        thread.started.connect(worker.run)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(thread.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker1Started)
        worker.progressed.connect(self.worker1Progressed)
        worker.finished.connect(self.worker1finished)

        thread.start()

    def worker1Started(self, value):
        self.b1.setDisabled(True)
        self.l1.setText(value)
        print('worker 1 iniciado', value)

    def worker1Progressed(self, value):
        self.l1.setText(value)
        print('1 em progresso', value)

    def worker1finished(self, value):
        self.b1.setEnabled(True)
        #  Ou
        # self.b1.setDisabled(False)
        self.l1.setText(value)
        print('worker 1 finalizado', value)

    def hardWork2(self):
        self._worker2 = Worker2()
        self._thread2 = QThread()

        # Isso garante que o widget vai ter uma referência para worker e thread
        worker = self._worker2
        thread = self._thread2

        # Worker é movido para a thread. Todas as funções e métodos do
        # objeto de worker serão executados na thread criado pela QThread.
        worker.moveToThread(thread)

        # Quando uma QThread é iniciada, emite o sinal started automaticamente.
        # Nome do método "doWork" modificado para "executeMe" (p/ exemplo)
        thread.started.connect(worker.executeMe)

        # O sinal finished é emitido pelo objeto worker quando o trabalho que
        # ele está executando é concluído. Isso aciona o método quit da qthread
        # que interrompe o loop de eventos dela.
        worker.finished.connect(thread.quit)

        # deleteLater solicita a exclusão do objeto worker do sistema de
        # gerenciamento de memória do Python. Quando o worker finaliza, ele
        # emite um sinal finished que vai executar o método deleteLater.
        # Isso garante que objetos sejam removidos da memória corretamente.
        thread.finished.connect(thread.deleteLater)
        worker.finished.connect(thread.deleteLater)

        # Aqui estão seus métodos e início, meio e fim
        # execute o que quiser
        worker.started.connect(self.worker2Started)
        worker.progressed.connect(self.worker2Progressed)
        worker.finished.connect(self.worker2finished)

        thread.start()

    def worker2Started(self, value):
        self.b2.setDisabled(True)
        self.l2.setText(value)
        print('2 iniciado', value)

    def worker2Progressed(self, value):
        self.l2.setText(value)
        print('2 em progresso', value)

    def worker2finished(self, value):
        self.b2.setEnabled(True)
        #  Ou
        # self.b1.setDisabled(False)
        self.l2.setText(value)
        print('2 finalizado', value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    myWidget.show()
    app.exec()
