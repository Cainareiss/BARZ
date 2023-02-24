class Cliente:

    def __init__(self, Nome, DT, TL):
        self.__Nome = Nome
        self.__DT = DT
        self.__TL = TL

    def Nome(self):
        self.__Nome = (str(input('Digite seu Nome:')))

    def DT(self):
        self.__DT = int(input('Digite sua data de nascimento:'))

    def TL(self):
        self.__TL = int(input('Digite seu telefone:'))

    def getNome(self):
        return self.__Nome

    def getDT(self):
        return self.__DT

    def getTL(self):
        return self.__TL

    def showAllData(self):
        return input((f"Dados da Pessoa:\nNome: {self.__Nome}\nData de Nascimento: {self.__DT}\nAltura: {self.__TL}"))


cliente = Cliente
print(Cliente)
print(cliente.Nome)
print(cliente.DT)
print(cliente.TL)
print(cliente.showAllData)
# print(cliente.Dados())
# print(cliente.DADOS('seus dados São:{}'.format()))
#
# #print('seus dados São:{}'.format(DADOS)
