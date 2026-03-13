while True:
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        break
    except ValueError:
        print("Digite apenas números.")

i = 1

while i <= 10:
    resultado = numero * i
    print(numero, "x", i, "=", resultado)
    i = i + 1