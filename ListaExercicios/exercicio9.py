#para esta ativiadade eu pensei que seria melhor somente os números inteiros serem lidos, assim eu poderia usar o try e except.

while True:
    n = input("\ninsira um valor inteiro: ")

    try:
        nValor = float(n)

        if nValor != int(nValor):
            print("Erro: Valor não corresponde a um inteiro! tente de novo.")
            continue

        else:
            print(f"{n} X 1 = {nValor * 1}")
            print(f"{n} X 2 = {nValor * 2}")
            print(f"{n} X 3 = {nValor * 3}")
            print(f"{n} X 4 = {nValor * 4}")
            print(f"{n} X 5 = {nValor * 5}")
            print(f"{n} X 6 = {nValor * 6}")
            print(f"{n} X 7 = {nValor * 7}")
            print(f"{n} X 8 = {nValor * 8}")
            print(f"{n} X 9 = {nValor * 9}")
            print(f"{n} X 10 = {nValor * 10}")

            break

    except ValueError:
        print("Erro: Apenas numeros são permitidos! evite texto.")

#eu entendi o motivo de não podermos usar laço de repetição, mas meu deus hein que negócio chato kkkkkkkkkkkkk