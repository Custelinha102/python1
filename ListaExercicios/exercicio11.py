import random

n = random.randint(0, 5)
# eu comecei a perder sem parar e não achava o número certo para poder verificar se o código estava correto, mas caso queira burlar isso apenas de um "print(n)" e seja feliz hehe
while True:

    try:
        chute = int(input("\nChute um valor para o número secreto de 0 a 5: "))

    except ValueError:
        print("Erro: Apenas numeros são permitidos! evite texto.")

    if chute < 0 or chute > 5:
        print("valor não permitido! tente de novo.")
        continue
    elif chute == n:
        print("Parabéns! você ganhou!")
        break
    else:
        print("poxa, você errou.")
        break

#depois de utilizar tanto esse try e except eu finalmente entedi: eu preciso ter no try somente aquilo que pode dar erro, como as coisas que o usuário digita, mas os "print" não! top