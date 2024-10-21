contadora = 1 
numeros = [] 
soma = 0
while (contadora<=6):
    numero = int(input(f"INSIRA O {contadora}º NÚMERO"))
    numeros.append(numero)
    soma += numero
    contadora +=1

media = soma/len(numeros)
print(f"A SOMA DOS NÚMEROS {numeros} é: {soma} e a media {media}")



