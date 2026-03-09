alturaParede = float(input("digite a altura da parede: "))
larguraParede = float(input("digite a largura da parede: "))
areaParede = alturaParede * larguraParede

print(f"a sua parede tem uma área de: {areaParede}m², para pintala serão necessários {(areaParede / 2)} baldes de tinta")

#minha lógica foi: se cada lata de tinta corresponde a 2m² então é só fazer a área da parede dividido por 2.