popA= 80000
popB=200000
ano = 0 


while popA<popB:
    ano +=1
    popA = 1 + 0.03 * popA
    popB = 1 + 0.015 *popB
    print("Ano %d:" % ano)
    print("Populaçao A: %d" % popA)
    print("População B: %d\n\n" % popB)
print("Ultrapassa no ano:",ano)