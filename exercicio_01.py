class Pessoa:
    def maiorIdade(self, idadePessoa):
        if idadePessoa > 18:
            return "Maior da idade!"
        else:
            return "Menor de idade!"

auxIdadePessoa = int(input("Digite a idade da pessoa: "))

p1 = Pessoa()
result = p1.maiorIdade(auxIdadePessoa)

print(result)