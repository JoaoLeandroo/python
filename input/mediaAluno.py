nome = input("Nome do Aluno: ")
n1 = float(input("Informe a primeira nota do Aluno: "))
n2 = float(input("Informe a segunda nota do aluno: "))
media = (n1+n2)/2

if media >= 7:
    print(f'Aluno Aprovado Media final {media}')
else:
    print(f'Aluno Reprovado Media final {media}')