class Cliente:

    def __init__(self, Nome='', DT='', TL=''):
        self.__Nome = Nome
        self.__DT = DT
        self.__TL = TL

    def setNome(self):
        self.__Nome = str(input('Digite seu Nome: '))

    def setDT(self):
        self.__DT = int(input('Digite sua data de nascimento: '))

    def setTL(self):
        self.__TL = int(input('Digite seu telefone: '))

    def getNome(self):
        return self.__Nome

    def getDT(self):
        return self.__DT

    def getTL(self):
        return self.__TL

    def showAllData(self):
        return (f"Dados da Pessoa:\nNome: {self.__Nome}\nData de Nascimento: {self.__DT}\nTelefone: {self.__TL}")


cliente = Cliente()
cliente.setNome()
cliente.setDT()
cliente.setTL()
print(cliente.showAllData())
