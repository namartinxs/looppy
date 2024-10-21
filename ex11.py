def collatz(numero):
    while numero != 1:
        if numero % 2 == 0:
            print(f"{numero} é par")
            numero = numero // 2  # Divisão inteira para manter o número como um inteiro
        else:
            print(f"{numero} é ímpar")
            numero = numero * 3 + 1
    return numero

# Chamando a função
if __name__ == '__main__':
    numero_inicial = 49
    collatz(numero_inicial)
