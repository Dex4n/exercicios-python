#9 - faça um método que receba um número X e uma palavra no console e repita x vezes a essa frase.

class Manipulacao:
    def mostrar_x_vezes(self, p_tamanho, p_texto):
        for i in range(p_tamanho):
            print(p_texto)

tamanho = int(input("Digite a quantidade de vezes que deseja repetir uma palavra: "))
texto = input("Agora digite a palavra desejada para repetir: ")

manipulador = Manipulacao()

resultado = manipulador.mostrar_x_vezes(tamanho, texto)

print(resultado)