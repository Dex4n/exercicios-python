#10 - receba três notas de um aluno e informe se ele passou ou reprovou.

class Aluno:
    
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def calcula_media(self):
        soma = self.n1 + self.n2 + self.n3
        media = soma / 3
        return media

nota1 = float(input("Digite uma nota para N1: "))
nota2 = float(input("Digite uma nota para N2: "))
nota3 = float(input("Digite uma nota para N3: "))

calcular = Aluno(nota1, nota2, nota3)

print("Média do aluno: (%.2f)" %calcular.calcula_media())