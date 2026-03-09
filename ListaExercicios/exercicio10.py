#eu sei fazer isso em java usando vetor, então vou tentar aplicar aqui tambèm


while True:
    try:
        n = [0, 0, 0]
        for i in range(3):
            n[i] = int(input(f"insira o valor do {i + 1}º número: "))
        tamanho = len(n)
        for i in range(tamanho):
            for j in range (tamanho -1):
                if n[j] < n[j + 1]:
                    temp = n[j]
                    n[j] = n [j + 1]
                    n[j + 1] = temp
        print(f"\nDo maior ao menor valor fica: {n}")
        print(f"Maior valor: {n[0]} --- Menor valor {n[2]}")
        break



    except ValueError:
        print("Erro: Apenas numeros são permitidos! evite texto.")

#eu realmente tenho que melhorar nos meus vetores em python, to até com medo de imaginar matriz kkkkkk, me acostumar com a syntaxe vai ser osso.
#OBS: eu gostei muito de bubble sort em java, mas aqui foi um pouco complicado para me acostumar.
