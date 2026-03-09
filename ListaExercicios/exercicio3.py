valorProduto = float(input("Insira o valor do produto para podermos aplicar um desconto de 5%!!!: "))
valorDesconto = valorProduto*0.05
produtoComDesconto = valorProduto - valorDesconto

print(f"o desconto foi de: {valorDesconto:.2f}R$\nSeu produto agora custa: {produtoComDesconto:.2f}R$")