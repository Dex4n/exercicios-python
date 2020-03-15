# 11 -  Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor.

class Numero:
    def __init__(self, numero):
        self.numero = numero

    def verificar_antecessor(self):
        antecessor = int
        antecessor = self.numero - 1
        return antecessor

numero = int(input("Digite um número para verificar o seu antecessor: "))

verificar = Numero(numero)

#print("Antecessor de {0} é {1}: ".format(numero, verificar.verificar_antecessor()))
print("Antecessor de (%d) é (%d): " %(numero, verificar.verificar_antecessor()))