while True:

    try:

        salarioBruto = float(input("Digite o salário: "))
        if salarioBruto < 0:
            print("Erro: Valor negativo! tente de novo.")
            continue
            
        else:
            salarioValorAumento = (salarioBruto * 0.15)
            salarioComAumento = (salarioBruto + salarioValorAumento)
            print(f"Seu novo salário com aumento de 15% é: {salarioComAumento}R$ !!!!")
            break

    except ValueError:
        print("Erro: Apenas numeros são permitidos! evite texto.")