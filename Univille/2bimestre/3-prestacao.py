# 3)	Efetuar o cálculo e a apresentação do valor de uma prestação em atraso, utilizando a fórmula: PRESTACAO = VALOR + (VALOR *(TAXA/100) * TEMPOEMDIAS).

valor = float(input("Digite o valor da prestação em atraso: "))

taxa = float(input("Digite o percentual da multa: "))

tempo = int(input("Digite o tempo em dias: "))

prestacao = valor + (valor * (taxa / 100) * tempo)

print(f"O valor da prestação em atraso é {prestacao:.2f}")