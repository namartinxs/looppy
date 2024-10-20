nota = float(input("Insira a nota "))

while (nota < 0) or (nota>10):
    nota = float(input("Nota deve estar dentro de 0-10 \nTente Novamente "))
print(f"{nota} é um valor valído")

