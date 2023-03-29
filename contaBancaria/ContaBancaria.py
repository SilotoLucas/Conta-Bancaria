class Conta:
    def __init__(self, id_conta, saldo):
        self.id_conta = id_conta
        self.saldo = saldo


class ContaCorrente(Conta):
    def __init__(self, id_conta, saldo, limite):
        super().__init__(id_conta, saldo)
        self.limite = limite
    
    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Saldo e limite insuficientes para realizar o saque.")
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")


class ContaPoupanca(Conta):
    def __init__(self, id_conta, saldo, taxa_de_rendimento):
        super().__init__(id_conta, saldo)
        self.taxa_de_rendimento = taxa_de_rendimento
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} realizado com sucesso. Novo saldo: {self.saldo}")
    
    def verificar_rendimento_ao_ano(self):
        rendimento = self.saldo * self.taxa_de_rendimento / 100
        print(f"O rendimento anual da conta é de {rendimento:.2f}.")



conta1 = ContaCorrente(1, 1000.0, 500.0)
conta1.depositar(200.0)
conta1.sacar(1500.0)
conta1.sacar(800.0)

conta2 = ContaPoupanca(2, 5000.0, 2.0)
conta2.depositar(1000.0)
conta2.verificar_rendimento_ao_ano()
   