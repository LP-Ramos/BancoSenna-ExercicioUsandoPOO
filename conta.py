from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    def detalhar(self):
        print()
        print(f'Agencia: {self.agencia}\n'
              f'Conta:  {self.conta}\n'
              f'Saldo: R${self.saldo:.2f}')
        print()

    def depositar(self, valor):
        if float(valor) < 0:
            print('Valor inválido')
            print()
            return
        self.saldo += float(valor)
        print(f'R${valor} depositado com sucesso.')
        self.detalhar()
        print()

    @abstractmethod
    def sacar(self, valor): pass


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo=0):
        super().__init__(agencia, conta, saldo)

    def sacar(self, valor):
        if float(self.saldo) < float(valor):
            print('Saldo insuficiente.')
            return
        self.saldo -= float(valor)
        print(f'Saque de R${valor} realizado com sucesso.')
        self.detalhar()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=500):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (float(self.saldo) + float(self.limite)) < float(valor):
            print('Saldo insuficiente.')
            print()
            return False
        self.saldo -= float(valor)
        print(f'Saque de R${valor} realizado com sucesso.')
        self.detalhar()
        return True
