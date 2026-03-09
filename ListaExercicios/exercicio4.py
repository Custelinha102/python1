#importando o módulo para facilitar minha vida né kkkk
import math

#só utilizei o try para tentar treinar e melhorar no que eu ainda não sei muito bem (usei IA para me explicar como usar e tentei aplicar sozinho)
try:
    valor = float(input("Insira um número para ver seu valor dobrado, triplicado e sua raiz: "))

    if valor < 0:
        print("ERRO: Impossível ver a raiz de um número negativo!")
    else:
        dobroValor = valor * 2
        triploValor = valor * 3
        raizValor = math.sqrt(valor)

        print(f"Dobro do valor: {dobroValor}\nTriplo do valor: {triploValor}\nRaiz do valor {raizValor}")

except ValueError:
    print("ERRO: Digite apenas números! o input recebeu texto.")

#Sinceramente eu sei que podia simplesmente fazer {valor * 2; valor * 3...}, mas eu quis fazer desta forma mesmo que seja contra intuitivo (já que não tem necessidade de fazer uma variável que não vou reutilizar para um exercicio tão besta), apenas por gosto pessoal ou talvez diversão, mas sei que poderia ter feito diferente.