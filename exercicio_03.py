#3 - Crie uma classe calculadora com as quatro operações básicas (soma, subtração, multiplicação e divisão).
# usuário deve informar dois números e o programa deve fazer as quatro operações.

class Calculadora:
    def soma (self, numero1, numero2):
        return numero1 + numero2

    def subtracao(self, numero1, numero2):
        return numero1 - numero2

    def multiplicacao(self, numero1, numero2):
        return numero1 * numero2

    def divisao(self, numero1, numero2):
        return numero1 / numero2

c1 = Calculadora()

soma = c1.soma(1,3)
divisao = c1.divisao(10,2)
multiplicacao = c1.multiplicacao(2,4)
subtracao = c1.subtracao(33,3)

print ("Resultado da soma: %.2f" %(soma))
print ("Resultado da divisão: %.2f" %(divisao))
print ("Resultado da multiplicação: %.2f" %(multiplicacao))
print ("Resultado da subtração: %.2f" %(subtracao))


