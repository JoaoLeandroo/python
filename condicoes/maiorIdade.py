
def suaIdade(age):
    if age >= 18:
        print(f'Você tem {age} anos, então pode entrar')
        return

    print(f'Você tem apenas {age} anos, você não pode entrar aqui.')


suaIdade(17)