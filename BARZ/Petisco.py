import Produto
class Petisco(Produto):
    def __init__(self, nome, preco, codigo, porcao, tipo, lactose):
        super().__init__(nome, preco, codigo)
        self.porcao = porcao
        self.tipo = tipo
        self.lactose = lactose

    def getPorcao(self):
        return self.porcao

    def setPorcao(self, porcao):
        self.porcao = porcao

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def isLactose(self):
        return self.lactose

    def setLactose(self, lactose):
        self.lactose = lactose
