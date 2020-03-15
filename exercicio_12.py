#12 - Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.


while True:
    n1 = int(input("Digite o 1º valor: "))
    n2 = int(input("Digite o 2º valor: "))

    if(n1 == n2):
        print("Você não pode digitar números iguais!")
        pass
    elif(n1 > n2):
        print("N1 é o maior!")
        break
    elif(n2 > n1):
        print("N2 é o maior!")
        break