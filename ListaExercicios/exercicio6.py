#vou fazer sem vetor pq to com preguiça de aprender vetor em python agora,mas em compensação vou fazer com try e except, fecho?   :)

while True:
    try:
        nota1 = float(input("insira valor da nota 1: "))
        nota2 = float(input("insira valor da nota 2: "))
        nota3 = float(input("insira valor da nota 3: "))
        nota4 = float(input("insira valor da nota 4: "))

        if min(nota1, nota2, nota3, nota4) < 0:
            print ("Erro: Valores negativos não são aceitos como nota, por favor tente de novo")
            continue

        else: print(f"Média: {(nota1 + nota2 + nota3 + nota4)/4:.2f}")
        break

    except ValueError:
        print("Erro: apenas numeros são permitidos! evite texto.")

#carai, esse demorou muito professor, meu deus hein... fritei meu cerebro com esse continue e break. Aliás eu utilizei o min() por conta da preguiça em ficar digitando "n1 or n2 or...", e o while foi um charme