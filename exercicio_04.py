#4 - Faça um programa que receba um valor que é o valor pago,
# um segundo valor que é o preço do produto e retorne o troco a ser dado.

class Troco:
    def calcularTroco(self, valorProduto, valorPago):

        if (valorPago == valorProduto):
            return "Não há necessidade de troco!"

        elif (valorPago < valorProduto):
            return "O cliente não pagou corretamente!"

        elif (valorPago > valorProduto):
            valorTroco = valorPago - valorProduto
            return "Valor de troco devido: " + str(valorTroco) + "!"

auxValorProduto = int(input("Digite o valor do produto: "))
auxValorPago = int(input("Digite o valor pago: "))

t1 = Troco()

result = t1.calcularTroco(auxValorProduto, auxValorPago)

print(result)