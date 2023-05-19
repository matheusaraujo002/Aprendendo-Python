nome = input("Escreva o seu nome: ")
salarioBase = float(input(f"Olá {nome}, Digite aqui o seu salário base: "))
tempo = float(input(f"{nome}, para finalizar, digite o tempo em anos que você está trabalhando na empresa: "))

if salarioBase < 200:
    novoSalario = salarioBase * 1
else:
    if salarioBase > 200 and salarioBase <= 450:
        imposto = salarioBase * 0.03
        novoSalario = salarioBase - imposto
    else:
        if salarioBase > 450 and salarioBase < 700:
            imposto = salarioBase * 0.08
            novoSalario = salarioBase - imposto
        else:
            if salarioBase == 700:
                imposto = salarioBase * 0.1
                novoSalario = salarioBase - imposto
            else:
                if salarioBase > 700:
                    imposto = salarioBase * 0.12
                    novoSalario = salarioBase - imposto

gratificacao = 0

if salarioBase > 500 and tempo <= 3:
    gratificacao = ((salarioBase * 1.02) - salarioBase) + 50
else:
    if salarioBase > 500 and tempo > 3:
        gratificacao = ((salarioBase * 1.03) - salarioBase) + 60
    else:
        if salarioBase <= 500 and tempo <= 3:
            gratificacao = ((salarioBase * 1.05) - salarioBase) + 23
        else:
            if salarioBase <= 500 and (tempo > 3 and tempo < 6):
                gratificacao = ((salarioBase * 1.06) - salarioBase) + 35
            else:
                if salarioBase <= 500 and tempo >= 6:
                    gratificacao = ((salarioBase * 1.1) - salarioBase) + 33

alimentacao = 0

if tempo <= 10:
    alimentacao = (salarioBase * 1.04) - salarioBase
else:
    if tempo > 10:
        alimentacao = (salarioBase * 1.06) - salarioBase

salarioLiquido = novoSalario + gratificacao + alimentacao

print(f"Olá {nome}, o seu salário após imposto foi de R${novoSalario:.2f}, você recebeu uma gratificação de R${gratificacao} por trabalhar {tempo:.0f} anos na nossa empresa e um auxilio alimentação de R${alimentacao}. Por fim seu salário liquido ficou em R${salarioLiquido}.")