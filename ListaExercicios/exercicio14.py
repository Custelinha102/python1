while True:
    try:
        velocidade = float(input("Digite a velocidade do carro: "))
        break
    except ValueError:
        print("Digite apenas números.")

limite = 120
multa_base = 130.16

if velocidade > limite:
    excesso = velocidade - limite
    valor = multa_base + (excesso * 7)
    print("O veículo foi multado.")
    print("Valor da multa: R$", valor)
else:
    print("Velocidade dentro do limite.")