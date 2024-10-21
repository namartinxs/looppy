user = input("Insira seu nome ")
pass_word = input("Insira a senha ")

while (user == pass_word):
    print("Acesso Negado\nTente novamente")
    user = input("Insira seu nome ")
    pass_word = input("Insira a senha ")

print("Acesso autorizado")