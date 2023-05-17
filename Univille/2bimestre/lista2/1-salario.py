""" 
1)	Faça um programa que receba o número de horas trabalhadas, o valor do salário mínimo e o número de horas extras trabalhadas. Calcule e mostre o salário a receber seguindo as regras abaixo:
a)	a hora trabalhada vale 1/8 do salário mínimo;
b)	a hora extra vale ¼ do salário mínimo;
c)	o salário bruto equivale ao número de horas trabalhadas multiplicado pelo valor da hora trabalha (apresente o valor para o usuário);
d)	a quantia a receber pelas horas extras equivale ao número de horas extras trabalhadas multiplicado pelo valor da hora extra(apresente o valor para o usuário);
e)	o salário a receber equivale ao salário bruto mais a quantia a receber pelas horas extras(apresente o valor para o usuário);
"""

numHoras = int(input("Digite o número de horas trabalhadas: "))
salarioMin = float(input("Digite o valor do salário minímo: "))
horasExtras = int(input("Digite o número de horas extras: "))

valorHora = salarioMin / 8
valorExtra = salarioMin / 4
salarioBruto = numHoras * valorHora
horaExtraTotal = valorExtra * horasExtras
salarioLiquido = salarioBruto + horaExtraTotal

print(f'O seu salário bruto é de R$ {salarioBruto:.2f}, você vai receber R$ {horaExtraTotal:.2f} por suas horas extras e seu salário liquido vai ser de R$ {salarioLiquido:.2f}')