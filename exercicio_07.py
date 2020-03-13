#7 - Escreva um algoritmo que leia 10 números informados pelo usuário e,
# depois, informe o menor, número, o maior número, a soma dos números
# informados e a média aritmética dos números informados.


class Numero:
    def ler_numeros(self):

        tamanho_range = 10
        contador = 1
        lista = []

        for i in range(tamanho_range):
            lista.append(float(input("Digite o %d° número " % contador)))
            contador += 1

        return lista

    def encontrar_maior(self, lista):

        maior = lista[0]

        for encontrar_maior in lista:
            if encontrar_maior > maior:
                maior = encontrar_maior
        return maior

    def encontrar_menor(self, lista):

        menor = lista[0]

        for encontrar_menor in lista:
            if encontrar_menor < menor:
                menor = encontrar_menor
        return menor

    def somar_valores(self, lista):

        soma_total = 0.0

        for valor in lista:
            soma_total += valor

        return soma_total

    def calcular_media(self, soma, lista):

        media_numeros = soma / len(lista)

        return media_numeros




#Instanciando uma variável do tipo da classe: Numero
numero = Numero()

#Criando uma variável que chama o método lerNumeros da classe Numero e atribui o retorno a variável criada
numeros_lista = numero.ler_numeros()



#print("Maior número: %d" %min(lista))

maior = numero.encontrar_maior(numeros_lista)
print("Maior número: %d" %maior)

#print("Menor número: %d" %max(lista))
menor = numero.encontrar_menor(numeros_lista)
print("Menor número: %d" %menor)

#print("Soma dos números: %d" %sum(lista))
soma = numero.somar_valores(numeros_lista)
print("Soma dos números: %.2f" %soma)

#print("Média dos números: #.2f" %(sum(lista) / len(lista)))
media = numero.calcular_media(soma, numeros_lista)
print("Média dos números: %.2f" %media)