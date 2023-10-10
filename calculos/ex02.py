from scipy.stats import kurtosis, skew

valores_1_2 = [1462.121, 1462.165]

valores_1_3 = [1462.121, 1462.165, 1462.071]

valores_1_4 = [1462.121, 1462.165, 1462.071, 1462.095]

valores_1_5 = [1462.121, 1462.165, 1462.071, 1462.095, 1462.097]

valores_1_6 = [1462.121, 1462.165, 1462.071, 1462.095, 1462.097, 1462.088]

valores_1_7 = [1462.121, 1462.165, 1462.071, 1462.095, 1462.097, 1462.088, 1462.163]

valores_1_8 = [1462.121, 1462.165, 1462.071, 1462.095, 1462.097, 1462.088, 1462.163, 1462.045]

valores_1_10 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097, 
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091
    ]

valores_1_15 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097, 
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091, 
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088
    ]

valores_1_20 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097,
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091, 
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088, 
    1462.057, 1462.081, 1462.094, 1462.144, 1462.085
    ]

valores_1_30 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097,
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091,
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088,
    1462.057, 1462.081, 1462.094, 1462.144, 1462.085,
    1462.115, 1462.113, 1462.071, 1462.078, 1462.126,
    1462.164, 1462.088, 1462.101, 1462.084, 1462.164
    ]
valores_1_40 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097,
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091,
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088,
    1462.057, 1462.081, 1462.094, 1462.144, 1462.085,
    1462.115, 1462.113, 1462.071, 1462.078, 1462.126,
    1462.164, 1462.088, 1462.101, 1462.084, 1462.164,
    1462.128, 1462.121, 1462.087, 1462.121, 1462.096,
    1462.106, 1462.13, 1462.107, 1462.051, 1462.118
]

valores_1_50 = [
    1462.121, 1462.165, 1462.071, 1462.095, 1462.097,
    1462.088, 1462.163, 1462.045, 1462.108, 1462.091,
    1462.052, 1462.056, 1462.145, 1462.085, 1462.088,
    1462.057, 1462.081, 1462.094, 1462.144, 1462.085,
    1462.115, 1462.113, 1462.071, 1462.078, 1462.126,
    1462.164, 1462.088, 1462.101, 1462.084, 1462.164,
    1462.128, 1462.121, 1462.087, 1462.121, 1462.096,
    1462.106, 1462.13, 1462.107, 1462.051, 1462.118,
    1462.096, 1462.122, 1462.034, 1462.117, 1462.021,
    1462.08, 1462.074, 1462.14, 1462.097, 1462.1
]


curtose_resultado = kurtosis(valores_1_10, fisher=False)
curtose_resultado2 = kurtosis(valores_1_10)

skew_resultado = skew(valores_1_3)

print("--------------------------------------")
print(f'Curtose Com Fisher: {curtose_resultado:.4f}')
print(f'Curtose SEM Fisher: {curtose_resultado2:.4f}')
print()
print(f'Assimetria: {skew_resultado:.4f}')
print("--------------------------------------")


