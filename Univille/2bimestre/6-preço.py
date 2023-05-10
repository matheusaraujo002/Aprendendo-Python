# 6)	Faça um programa que receba o preço de um produto, calcule e mostre, de acordo com as tabelas a seguir, o novo preço e a classificação.
'''
Preço	                                   Percentual Aumento
Até R$ 50,00	                                    5
Entre R$ 50,00 e R$ 100,00	                        10
Acima de R$ 100,00	                                15

Novo preço	                                  Classificação
Até R$ 80,00	                                  Barato
Entre R$ 80,00 e R$120,00(inclusive)	          Normal
Entre R$ 120,00 e R$ 200,00 (inclusive)	           Caro
Maior que R$ 200,00	                            Muito Caro
'''

preço = float(input("Digite o preço do produto: R$ "))
if preço <= 50:
    aumento = preço * 0.05
    ajuste = preço + aumento
else:
    if preço >= 50 and preço <= 100:
        aumento = preço * 0.1
        ajuste = preço + aumento
    else:
        if preço > 100:
            aumento = preço * 0.15
            ajuste = preço + aumento

if ajuste <= 80:
    classificacao = 'Barato'
    print(f'O novo preço é de R${ajuste:.2f} e a classificação é {classificacao}')
else:
    if ajuste >= 80 and ajuste <= 120:
        classificacao = 'Normal'
        print(f'O novo preço é de R${ajuste:.2f} e a classificação é {classificacao}')
    else:
        if ajuste >= 120 and ajuste <= 200:
            classificacao = 'Caro'
            print(f'O novo preço é de R${ajuste:.2f} e a classificação é {classificacao}')
        else:
            if ajuste > 200:
                classificacao = 'Muito Caro'
                print(f'O novo preço é de R${ajuste:.2f} e a classificação é {classificacao}')