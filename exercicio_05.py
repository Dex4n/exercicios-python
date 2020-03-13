#5 - Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo), se é par ou ímpar

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