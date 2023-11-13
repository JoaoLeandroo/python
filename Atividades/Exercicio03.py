# variavel para receber a media de determinado ano gerada no exercicio 2, a medita utilizada no exemplo é do ano 1995
media_ano_chmsl = -21.736
# Váriavel que recebe a soma total das medias geradas nos anos de 1995 até 2018, script para gerar essa media está em media_total.py
media_total_chsml_1995_a_2018 = 11.200
# Váriavel para fazer o calculo dessas medias
soma = media_ano_chmsl - media_total_chsml_1995_a_2018
print(f'Soma chmsl {soma}')


media_ano_sst = 0.47
sst_media_total_1995_a_2018 = 0.641
soma_sst = media_ano_sst - sst_media_total_1995_a_2018
print(f'Soma sst {round(soma_sst, 3)}')


calculo_final = soma * soma_sst
print(round(calculo_final, 3))