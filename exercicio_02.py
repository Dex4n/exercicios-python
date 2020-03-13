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

auxColetaNumero = int(input("Digite um número de 1 até 5 \n"))

n1 = Numero()
result = n1.escreverExtenso(auxColetaNumero)

print (result)