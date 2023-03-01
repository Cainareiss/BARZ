import re
from datetime import date
import Cliente, Compra, Bebida, Petisco


def main():
    print("====Seja bem vindo====")
    nome = input("Digite seu nome: ")
    formato = r"\d{2}/\d{2}/\d{4}"
    fomato_correto = bool(re.match(formato, input("Digite sua data de nascimento(dd/mm/AAAA): ")))

    try:
        if not fomato_correto:
            raise Exception("Formato de data inválido")
        else:
            data_nascimento = date(2002, 5, 15)
            telefone = input("Digite seu telefone: ")
            cliente = Cliente(nome, data_nascimento, telefone)

            compra = Compra(cliente)
            produto1 = Bebida("Cachaça", 15.0, 1, "Ypióca", 1, True)
            produto2 = Bebida("Refrigerante", 5, 2, "Coca Cola", 1, False)
            produto3 = Petisco("Bacon", 8.0, 3, 1, "Não vegetariano", False)

            compra.incluir_produto(produto1)
            compra.incluir_produto(produto2)
            compra.incluir_produto(produto3)

            total = compra.somar_conta()
            valor = 100.0
            troco = compra.pagar_conta(valor, total)

            print(f"Você pagou: {valor}")
            print(f"Sua conta é: {total}")
            print(f"Seu troco é: {troco}")

    except Exception as e:
        print(e)
        print("Fechando o programa.")


if __name__ == "__main__":
    main()
