def calcular_imc (peso, altura):

    imc = peso / (altura * altura)
    imc = round(imc, 2)

    return imc
