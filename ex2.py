'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações'''
user = input("Insira seu nome ")
pass_word = input("Insira a senha ")

while (user == pass_word):
    print("Acesso Negado\nTente novamente")
    user = input("Insira seu nome ")
    pass_word = input("Insira a senha ")

print("Acesso Autorizado")