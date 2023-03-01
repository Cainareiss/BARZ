import re
from datetime import date
from Cliente import Cliente
from Compra import Compra
from Bebida import Bebida
from Petisco import Petisco


def selecionar_produto(lista_produtos):
    """Apresenta a lista de produtos e solicita que o usuário selecione um."""
    print("==== Lista de Produtos ====")
    for i, produto in enumerate(lista_produtos):
        print(f"{i + 1} - {produto.get_nome()} - R${produto.get_preco()}")
    print("===========================")

    # Solicita a seleção do usuário
    while True:
        try:
            opcao = int(input("Digite o número do produto que deseja adicionar à compra: "))
            if opcao < 1 or opcao > len(lista_produtos):
                raise ValueError()
            return lista_produtos[opcao - 1]
        except ValueError:
            print("Opção inválida. Digite novamente.")


def main():
    print("==== Seja bem vindo ====")
    nome = input("Digite seu nome: ")
    formato = r"\d{2}/\d{2}/\d{4}"
    formato_correto = bool(re.match(formato, input("Digite sua data de nascimento(dd/mm/AAAA): ")))

    try:
        if not formato_correto:
            raise Exception("Formato de data inválido")
        else:
            data_nascimento = date(2002, 5, 15)
            telefone = input("Digite seu telefone: ")
            cliente = Cliente(nome, data_nascimento, telefone)

            compra = Compra(cliente)

            # Lista de produtos disponíveis
            produtos_disponiveis = [
                Bebida("Cachaça", 15.0, 1, "Ypióca", 1, True),
                Bebida("Refrigerante", 5, 2, "Coca Cola", 1, False),
                Petisco("Bacon", 8.0, 3, 1, "Não vegetariano", False)
            ]

            # Solicitação dos produtos que o cliente deseja adicionar à compra
            while True:
                produto_selecionado = selecionar_produto(produtos_disponiveis)
                compra.incluir_produto(produto_selecionado)
                print(f"Produto '{produto_selecionado.get_nome()}' adicionado à compra.")

                # Pergunta se o cliente deseja adicionar mais produtos
                opcao_continuar = input("Deseja adicionar mais produtos? (s/n) ")
                if opcao_continuar.lower() != "s":
                    break

            # Finalização da compra
            total = compra.somar_conta()
            valor = float(input("Digite o valor pago pelo cliente: R$"))
            troco = compra.pagar_conta(valor, total)
            print(f"Você pagou: R${valor}")
            print(f"Sua conta é: R${total}")
            print(f"Seu troco é: R${troco:.2f}")

    except Exception as e:
        print(e)
        print("Fechando o programa.")


if __name__ == "__main__":
    main()
