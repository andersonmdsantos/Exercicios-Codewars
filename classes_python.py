class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    def setNome(self, nome):
        self.nome = nome
    def setRg(self, rg):
        self.rg = rg
    def setIdade(self, idade):
        self.idade = idade
    def getNome(self):
        return self.nome
    def getRg(self):
        return self.rg
    def getIdade(self):
        return self.idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Maria", 1234567890, 30)
pessoa1.apresentar()  # Chamando o método da instância


## from pessoa import Pessoa
class PessoaJuridica(Pessoa):
    def __init__(self, cnpj, nome, rg, idade):
        super().__init__(nome, rg, idade)
        self.cnpj = cnpj
    def getCnpj(self):
        return self.cnpj
    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    
pessoacnpj = PessoaJuridica(12, "João", 34, 56)
pessoacnpj.apresentar()
