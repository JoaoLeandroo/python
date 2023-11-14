# variavel para receber a media de determinado ano gerada no exercicio 2, a media utilizada no exemplo é do ano 1995
media_ano_chmsl = -21.736
# Váriavel que recebe a soma total das medias geradas nos anos de 1995 até 2018, script para gerar essa media está em media_total.py
media_total_chsml_1995_a_2018 = 11.200
# Váriavel para fazer o calculo dessas medias
somaChmsl = media_ano_chmsl - media_total_chsml_1995_a_2018
print(f'Soma chmsl total {somaChmsl}')

# Variavel para receber a media anual do sst de acordo com o mesmo ano da media do chmsl
media_ano_sst = 0.47
# Variável para receber a media total do sst de 1995 até 2018
sst_media_total_1995_a_2018 = 0.641
# Variável que faz a subtração da media anual do sst e das medias totais de 1995 até 2018
soma_sst = media_ano_sst - sst_media_total_1995_a_2018
print(f'Soma sst total {round(soma_sst, 3)}')


# Aqui é calculado a covariancia entre as duas variaveis
calculo_final = somaChmsl * soma_sst
print(f'Covariancia: {round(calculo_final, 3)}')

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
# o metodo len verifica quantos elementos existem dentro do array
# na variável abaixo esta pegando o resultando da covariacia e fazendo a divisão pela quantidade de elementos(24)
resp_covariancia = resultadoVarianciaTotal / len(dadosCovariancia)
# Resultado final
print(f'Resultado Final: {resp_covariancia - 1}')
