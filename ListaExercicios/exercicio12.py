#poxa, nesse vou precisar pesquisar, mas vou tentar entender.

while True:
    try:
        ano = int(input("digite um ano: "))
        break
    except ValueError:
        print("Digite apenas números! evite texto.")

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print("Ano bissexto")
else:
    print("Não é ano bissexto")

#noooossa, bem fácil, se eu conseguir memorizar a regra gg. Aliás, pensei agora: dependendo da identação o while para sem parar o sitema todo, top d+