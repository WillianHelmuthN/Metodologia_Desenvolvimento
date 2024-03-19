def calcular_imc (peso, altura):

    imc = peso / (altura * altura)
    imc = round(imc, 2)

    return imc

peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

resultado_imc = calcular_imc(peso, altura)

print(f"Seu IMC é {resultado_imc:.2f}")