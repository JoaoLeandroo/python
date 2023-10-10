import numpy as np
import matplotlib.pyplot as plt
import statistics

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

media = statistics.mean(valores_1_50)

residuos = []
for i in valores_1_50:
    residuo = -media + i
    residuos.append(residuo)

plt.title('DISTÂNCIAS')
plt.xlabel('Distâncias (m)')
plt.ylabel('Frequência')
plt.hist(valores_1_50, rwidth=0.5, color='blue')
plt.show()
print()
plt.title('REDÍDUOS')
plt.xlabel('Resíduos (m)')
plt.ylabel('Frequência')
plt.hist(residuos, rwidth=0.5, color='red')
plt.show()
print()
print('Resíduos:')
print(np.transpose(residuos))
