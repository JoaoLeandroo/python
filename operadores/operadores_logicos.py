
# Os dois resultados precisam ser verdadeiros
numero = 10
numero2 = 11
if numero == 10 and numero >= numero2:
    print("Passou no teste...")
else:
    print("Deu ruim...")


# se um dos resultados for True a condição é atendida
nome = "ola"
nome2 = "mundo"
if nome == "ola" or nome2 == "mundo":
    print("Nome passou...")
else:
    print("Os dois nomes sao diferente")


# Negação
condicao = False
if not condicao:
    print("A condição é False.")
else:
    print("A condição é True.")