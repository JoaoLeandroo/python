#  :s - texto string
#  :d - números inteiros
#  :f - números flutuantes
#  :.(NUMERO)f - quantidade de casas decimais Float
#  :(CARACTERE) (> ou < ou ^) (QUANTIDADE) (TIPO - s d ou f)

numero_1 = 10
numero_2 = 3

divisao = numero_1 / numero_2
print(divisao)
print('{:.2f}'.format(divisao))

teste = "numero Final"
print(f'{teste} {divisao:.1f}')

nome = "João Leandro"
print(f'{nome:.3s}')