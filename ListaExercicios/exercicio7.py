while True:
    try:
        metros = float(input("\ndigite a quantidade de metros: "))
        centimetros = (metros*100)
        milimetros = (metros*1000)

        if metros < 0:
            print("Erro: Valor negativo! tente de novo.")
            continue
        else:
            print(f"{metros}m é exatamente {centimetros}cm ou {milimetros}mm")
            break
    except ValueError:
        print("Erro: Apenas numeros são permitidos! evite texto.")