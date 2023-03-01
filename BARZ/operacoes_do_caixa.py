#@abstractmethod
def pagarConta(self, valor: float, total: float) -> float:
    pass

#@abstractmethod
def somarConta(self) -> float:
    pass

#@abstractmethod
def removerProduto(self, produto: Produto) -> None:
    pass

#@abstractmethod
def incluirProduto(self, produto: Produto) -> None:
    pass
