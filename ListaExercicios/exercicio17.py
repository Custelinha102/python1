palavra = input("Digite uma palavra: ").lower()

contador = 0

for letra in palavra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador = contador + 1

print("Quantidade de vogais:", contador)