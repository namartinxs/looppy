numero_maximo = int(input("INSIRA O NUMERO DE PARADA "))

for n in range(2,numero_maximo+1):
    primo = True
    for i in range(2,n):
        if n %i == 0:
            primo = False

    if primo != False:
        print (n)

