#classe base sem instancia
#class Carro:
#    pass # ainda vazia, só o modelo

#Como criar objetos (instancia)
class Carro:
    def __init__(self,marca):
        self.marca = marca

meu_carro = Carro("Toyota") #criando objeto(instância)
print(type(meu_carro))
print(meu_carro.marca)

#Encapsulamento
class Banco:
    def __init__(self,saldo=0):
        self.saldo = saldo

    @property
    def saldo_E50(self):
        return self.saldo

    def depositar(self,valor):
        if valor <=0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor

    def sacar(self,valor):
        if valor <=0:
            raise ValueError("Valor deve ser positivo") 
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")  
        self.saldo -= valor
    
banco_master = Banco(100)
print(banco_master.saldo_E50)
banco_master.depositar(150)
print("saldo atual:",banco_master.saldo_E50)
banco_master.sacar(50)
print("saldo atual:",banco_master.saldo_E50)
       
class Conta(Banco):
    def __init__(self,num_conta,cliente,saldo=0,agencia=455):
        super().__init__(saldo)
        self.agencia = agencia
        self.num_conta = num_conta
        self.cliente = cliente

    def __str__(self):
        return f"Agencia: {self.agencia}\n Conta:{self.num_conta} \n Nome: {self.cliente}"
    
conta1 = Conta("254567897545-5","Bruno Gomes",357,452)
conta2 = Conta("254567897545-5","Luana Prazeires",1000000)

print(conta1,f"\n saldo:",conta1.saldo_E50)
print("Saldo:",conta1.saldo_E50)
print(conta2,f"\n saldo:",conta2.saldo_E50)