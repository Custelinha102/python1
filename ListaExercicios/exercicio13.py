while True:
    try:
        numero = int(input("\nDigite um número inteiro: "))
        break
    except ValueError:
        print("Erro: apenas números inteiros são permitidos! Evite texto.")
        continue

print("\nbases de conversão")
print("1 - binário")
print("2 - octal")
print("3 - hexadecimal")

while True:
    try:
        baseConversao = int(input("escolha para qual base voce quer converter o valor: "))
        
        if baseConversao == 1:
            print(f"\nO número {numero} em binário fica: {bin(numero)[2:]}")
            break
        elif baseConversao == 2:
            print(f"\nO número {numero} em octal fica: {oct(numero)[2:]}")
            break
        elif baseConversao == 3:
            print(f"\nO número {numero} em hexadecimal fica: {hex(numero)[2:]}")
            break
        else:
            print("Erro: Escolha uma opção entre 1, 2 ou 3.")
            
    except ValueError:
        print("Erro: apenas os valores da base são permitidos! Evite texto.")
