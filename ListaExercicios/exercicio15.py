while True:
    try:
        distancia = float(input("Digite a distância da viagem em km: "))
        break
    except ValueError:
        print("Digite apenas números.")

if distancia <= 200:
    preco = distancia * 7.50
else:
    preco = distancia * 5.35

print("Preço da passagem: R$", preco)