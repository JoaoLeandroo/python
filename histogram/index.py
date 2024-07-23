import matplotlib.pyplot as plt

# Dados
muitoAlto = 7.709614
alta = 3.216926
moderada = 1.734289
baixo = 1.550852
muitoBaixo = 0.245165

dados = [muitoAlto, alta, moderada, baixo, muitoBaixo]

# Rótulos para as categorias
labels = ['Muito Alto', 'Alta', 'Moderada', 'Baixo', 'Muito Baixo']

# Calculando as porcentagens
total = sum(dados)
percentagens = [(dado / total) * 100 for dado in dados]

# Criando a figura e o eixo
fig, ax1 = plt.subplots(figsize=(10, 6))

# Plotando os dados no eixo y da esquerda (percentagens)
bars = ax1.bar(labels, percentagens, color='skyblue', label='Porcentagem')
ax1.set_ylabel('Porcentagem (%)')
ax1.set_ylim(0, max(percentagens) * 1.1)

# Criando um segundo eixo y compartilhando o mesmo eixo x
ax2 = ax1.twinx()
line, = ax2.plot(labels, dados, color='red', marker='o', label='Área')
ax2.set_ylabel('Área (km²)')
ax2.set_ylim(0, max(dados) * 1.1)

# Adicionando título e rótulos aos eixos
plt.title('')

# Adicionando a legenda
bars.set_label('Porcentagem')
ax1.legend(loc='upper right', bbox_to_anchor=(0.5, -0.1), ncol=2)

line.set_label('Área')
ax2.legend(loc='upper left', bbox_to_anchor=(0.5, -0.1), ncol=2)

# Ajustando o layout para que a legenda não sobreponha o gráfico
plt.tight_layout(rect=[0, 0, 1, 0.95])

# Exibindo o gráfico
plt.show()
