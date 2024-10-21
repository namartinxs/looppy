contadora = 1 
numeros =[] 
maior = 0
while (contadora<=5):
    numero = int(input(f"INSIRA O {contadora}º NÚMERO"))
    numeros.append(numero)
    if numero > maior:
        maior =numero
    contadora +=1

print(f"TODOS OS NÚMEROS:{numeros}")
print(f"O MAIOR ENTRE TODOS OS NÚMEROS É: {maior}")
