nome = input("Escreva o seu nome: ")
salarioBase = float(input("Olá {nome}, Digite aqui o seu salário base: "))
tempo = float(input("{nome}, para finalizar, digite o tempo em anos que você está trabalhando na empresa: "))

if salarioBase < 200:
    novoSalario = salarioBase * 1
else:
    if salarioBase > 200 and salarioBase <= 450:
        novoSalario = salarioBase * 1.03
    else:
        if salarioBase > 450 and salarioBase < 700:
            novoSalario = salarioBase * 1.08
        else:
            if salarioBase == 700:
                novoSalario = salarioBase * 1.1
            else:
                if salarioBase > 700:
                    novoSalario = salarioBase * 1.12

gratificacao = 0

if salarioBase > 500 and tempo <= 3:
    gratificacao = (salarioBase * 1.02) + 50
else:
    if salarioBase > 500 and tempo > 3:
        gratificacao = (salarioBase * 1.03) + 60
    else:
        if salarioBase <= 500 and tempo <= 3:
            gratificacao = (salarioBase * 1.05) + 23
        else:
            if salarioBase <= 500 and (tempo > 3 and tempo < 6):
                gratificacao = (salarioBase * 1.06) + 35
            else:
                if salarioBase <= 500 and tempo >= 6:
                    gratificacao = (salarioBase * 1.1) + 33

alimentacao = 0

if tempo <= 10:
    alimentacao = (salarioBase * 1.04)
else:
    if tempo > 10:
        alimentacao = (salarioBase * 1.06)

salarioLiquido = novoSalario + gratificacao

print(f"Olá {nome}, o seu salário após imposto foi de {novoSalario:.2f}, Você recebeu uma gratificação de {gratificacao} por trabalhar {tempo} anos na nossa empresa e um auxilia alimentação de {alimentacao}.")