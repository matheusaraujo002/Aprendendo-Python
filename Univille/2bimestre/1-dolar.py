# 1) Elaborar um programa que efetue o cálculo do valor da conversão em real (R$) de um valor lido em tela em dólar (US$). O programa deverá solicitar o valor da cotação do dólar.

valorDolar = float(input("Digite aqui o valor da cotação do dólar: "))

dolarSolicitado = float(input("Digite aqui quantos dólares você quer converter: "))

conversao = valorDolar * dolarSolicitado

print(f"{dolarSolicitado} dólares convertido para real é igual à R$ {conversao}")