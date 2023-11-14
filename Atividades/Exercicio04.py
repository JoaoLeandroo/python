# Array com os dados do chmsl
soma_chmsl = [
    [-32.936], [-30.672], [-27.520], [-29.173], [-26.060], [-23.049], [-17.401], 
    [-14.107], [-11.351], [-8.433], [-3.426], [-2.266], [-2.279], [1.386], [5.827], 
    [7.191], [6.432], [16.973], [19.403], [23.386], [33.255], [35.975],
    [37.373], [41.483]
]

# Array vazio que irá receber os dados multiplicados do chmsl
new_array_chmsl = []
# for para rodar cada elemento da lista e fazer a sua multiplicação e inserir esses esses elementos na lista atraves da variavel cont
soma = 0
soma2 = 0
for i in soma_chmsl:
    soma = i[0]
    soma2 = i[0]
    cont = soma * soma2
    # o metodo append adiciona um elemento ao final do array
    new_array_chmsl.append([round(cont, 3)])

# apos inserir todos os dados no new_array_chmsl, esse for irá somar todos os elementos do array
somador_final_chmsl = 0
for entrada in new_array_chmsl:
    somador_final_chmsl += entrada[0]

print(f'Dados totais do new_array_chmsl: {round(somador_final_chmsl, 4)}')


# array com os dados do sst
soma_sst = [
    [-0.172], [-0.322], [-0.122], [-0.008], [-0.202], [-0.212], [-0.072], [-0.022],
    [-0.002], [-0.062], [0.028], [-0.002], [-0.022], [-0.102], [0.008], [0.088], [-0.062],
    [-0.002], [0.038], [0.098], [0.288], [0.358], [0.268], [0.188]
]

cont_sst = 0
const_sst_2 = 0
# Array vazio que irá receber os dados multiplicados do sst
new_array_sst = []
# for para percorrer a lista e adicionar os itens ao new_array_sst
for entrada in soma_sst:
    cont_sst = entrada[0]
    cont_sst_2 = entrada[0]
    cont = cont_sst * cont_sst_2
    new_array_sst.append([round(cont, 4)])

# For para percorrer os dados do new_array_sst e somar todos os seus elementos
somador_final_sst = 0
for entrada in new_array_sst:
    somador_final_sst += entrada[0]
print(f'Dados totais do new_array_sst: {somador_final_sst}')

# Variaveis para calcular a Raiz Quadrada do valor total dos new_array_chmsl e new_array_sst
contRaizQ = somador_final_chmsl * somador_final_sst
resultadoRaizQ = contRaizQ ** 0.5
print(f'Raiz Quadrada: {resultadoRaizQ}')

# Lista(array) com os dados da covariancia de cada ano
dadosCovariancia = [
    [1995, 5.632], [1996, 9.846], [1997, 3.33], [1998, -0.263], [1999, 5.238], [2000, 4.863], [2001, 1.235], [2002, 0.296], [2003, 0.011],
    [2004, 0.514], [2005, 0.099], [2006, 0.002], [2007, 0.048], [2008, -0.140], [2009, 0.052], [2010, 0.640], [2011, -0.392], [2012, -0.017],
    [2013, 0.757], [2014, 2.315], [2015, 9.611], [2016, 12.915], [2017, 10.053], [2018, 7.84] 
]

# Aqui é a lista dadosCovariancia é percorrida e cada dado é somado a variável resultadoVarianciaTotal declarada fora do loop de repetição
resultadoVarianciaTotal = 0
for entrada in dadosCovariancia:
    resultadoVarianciaTotal += entrada[1]

# Aqui é imprimido na tela o valor total
print(f'Covariancia total: {resultadoVarianciaTotal}')
# a váriavel resultadoFinal recebe os dados totais da covariancia(74.485) e divide pela raizQuadrada do somador_final_chmsl e somador_final_sst
resultadoFinal = resultadoVarianciaTotal / resultadoRaizQ
# Aqui a resposta final é imprimida na tela
print(f'RESPOSTA FINAL: {round(resultadoFinal, 5)}')