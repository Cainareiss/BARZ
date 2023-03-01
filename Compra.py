from typing import List
from operacoes_do_caixa import OperacoesDoCaixa
from produto import Produto
from cliente import Cliente


class Compra(OperacoesDoCaixa):
    def __init__(self, cliente: Cliente):
        self.listaProdutos: List[Produto] = []
        self.total: float = 0.0
        self.cliente: Cliente = cliente

    def get_lista_produtos(self) -> List[Produto]:
        return self.listaProdutos

    def set_lista_produtos(self, lista_produtos: List[Produto]) -> None:
        self.listaProdutos = lista_produtos

    def get_total(self) -> float:
        return self.total

    def set_total(self, total: float) -> None:
        self.total = total

    def get_cliente(self) -> Cliente:
        return self.cliente

    def set_cliente(self, cliente: Cliente) -> None:
        self.cliente = cliente

    def remover_produto(self, produto: Produto) -> None:
        for p in self.listaProdutos:
            if p.get_codigo() == produto.get_codigo():
                self.listaProdutos.remove(p)

    def incluir_produto(self, produto: Produto) -> None:
        self.listaProdutos.append(produto)

    def pagar_conta(self, valor: float, total: float) -> float:
        troco = valor - total
        return troco

    def somar_conta(self) -> float:
        total = 0.0
        for produto in self.listaProdutos:
            total += produto.get_preco()
        return total
