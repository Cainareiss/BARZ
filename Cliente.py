from datetime import datetime

class Cliente:
    def __init__(self, Nome='', DT='', TL=''):
        self.__Nome = Nome
        self.__DT = DT
        self.__TL = TL

    class Cliente:
        def __init__(self, Nome='', DT='', TL=''):
            self.__Nome = Nome
            self.__DT = DT
            self.__TL = TL

        def setNome(self):
            self.__Nome = str(input('Digite seu Nome: '))

        def setDT(self):
            while True:
                data_texto = input('Digite sua data de nascimento (Dia/Mes/Ano): ')
                if len(data_texto) == 10:
                    try:
                        data_objeto = datetime.strptime(data_texto, '%d/%m/%Y')
                        self.__DT = data_objeto.strftime('%d-%m-%Y')
                        break
                    except ValueError:
                        print('Data inválida. Tente novamente.')
                else:
                    print('A data deve ter 10 caracteres (dd/mm/aaaa). Tente novamente.')

        def setTL(self):
            while True:
                telefone = input('Digite seu telefone: ')
                if len(telefone) == 11:
                    try:
                        self.__TL = int(telefone)
                        break
                    except ValueError:
                        print('Número de telefone inválido. Tente novamente.')
                else:
                    print('O número de telefone deve ter 10 dígitos. Tente novamente.')

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
