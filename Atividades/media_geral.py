
# A variável sst é uma lista de listas, onde cada sublista contém dois elementos: o primeiro elemento da lista é o ano e o segundo é um valor associado a esse ano.
sst = [
    [1995, 0.47], [1996, 0.32], [1997, 0.52], [1998, 0.65], [1999, 0.44],
    [2000, 0.43], [2001, 0.57], [2002, 0.62], [2003, 0.64], [2004, 0.58],
    [2005, 0.67], [2006, 0.64], [2007, 0.62], [2008, 0.54], [2009, 0.65],
    [2010, 0.73], [2011, 0.58], [2012, 0.64], [2013, 0.68], [2014, 0.74],
    [2015, 0.93], [2016, 1], [2017, 0.91], [2018, 0.83]
]

soma = 0
for i in range(len(sst)):
    soma += sst[i][1]

media = soma / len(sst)
print(f'Media sst: {round(media, 4)}')



# Dados com os resultados das medias anuais de 1995 até 2018 de acordo com os dados da chmsl
mediaTotal = [
    [1995, -21.736], [1996, -19.472], [1997, -16.32], [1998, -17.973], [1999, -14.86], [2000,-11.849], 
    [2001, -6.201], [2002, -2.907], [2003, -0.151], [2004, 2.767], [2005, 7.774], [2006, 8.934], [2007, 8.921],
    [2008, 12.586], [2009, 17.027], [2010, 18.391], [2011, 17.632], [2012, 28.173], [2013, 30.603], [2014, 34.586],
    [2015, 44.455], [2016, 47.175], [2017, 48.573], [2018, 52.683]
]

soma3 = 0
for i in range(len(mediaTotal)):
    soma3 += mediaTotal[i][1]

media3 = soma3 / len(mediaTotal)
print(round(media3, 4))

