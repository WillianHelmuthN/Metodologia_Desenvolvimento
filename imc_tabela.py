def calcular_imc (peso, altura):

    imc = peso / (altura * altura)
    imc = round(imc, 2)

    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Magreza"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade grau I"
    elif 35 <= imc < 40:
        return "Obesidade grau II"
    else:
        return "Obesidade grau III"