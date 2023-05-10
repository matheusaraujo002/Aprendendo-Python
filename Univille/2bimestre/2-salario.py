# 2)	Construir um programa que efetue o cálculo do salário líquido de um professor. Para fazer este programa, você deverá possuir alguns dados, tais como: valor da hora aula, número de horas trabalhadas no mês e percentual de desconto do INSS. Em primeiro lugar, deve-se estabelecer qual será o seu salário bruto para efetuar o desconto e ter o valor do salário líquido.

horaAula = float(input("Digite o valor da hora aula: "))

horasTrabalhadas = int(input("Digite o número de horas trabalhadas no mês: "))

percentualDesconto = float(input("Digite o percentual de desconto do INSS: "))

salarioBruto = horaAula * horasTrabalhadas

desconto = (salarioBruto * percentualDesconto) / 100

salarioLiquido = salarioBruto - desconto

print(f"O salário líquido é: R$ {salarioLiquido:.2f}")

