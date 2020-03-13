#6 - Faça um algoritmo que leia um nº inteiro e mostre uma mensagem indicando se este número é par ou ímpar, e se é positivo ou negativo


number = int(input("Digite um número: \n"))

if (number >= 0):
    print("O número (%d) digitado é positivo!" %(number))
    if (number % 2 == 0):
        print("O número (%d) é par!" % (number))
    else:
        print("O número (%d) é ímpar!" % (number))

elif (number < 0):
    print("O número (%d) digitado é negativo!" %(number))
    if (number % 2 == 0):
        print("O número (%d) é par!" % (number))
    else:
        print("O número (%d) é ímpar!" % (number))