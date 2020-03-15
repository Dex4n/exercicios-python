class Numero:

    def escreverExtenso(self, numero):
        if (numero == 1):
            return "um"
        elif (numero == 2):
            return "dois"
        elif (numero == 3):
            return "três"
        elif (numero == 4):
            return "quatro"
        elif (numero == 5):
            return "cinco"

while True:
    auxColetaNumero = int(input("Digite um número de 1 até 5 para escrever por extenso: "))
    if (auxColetaNumero < 1 or auxColetaNumero > 5):
        print("Você digitou um valor inválido!")

    else: break

n1 = Numero()
result = n1.escreverExtenso(auxColetaNumero)

print (result)