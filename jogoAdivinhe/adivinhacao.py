print('___________________________________________________________________________')
print('Bem vindos ao jogo de adivinhação!!')
print('___________________________________________________________________________')

import random

numero_secreto = random.randrange(1, 101)
tentativas = 0
contador = 0

print('Escolha a dificuldade')
dificuldade = int(input('[1] FÁCIL - [2] MÉDIO - [3] DIFÍCIL: '))

if dificuldade == 1:
    tentativas = 20
    print('___________________________________________________________________________')
    print('Você terá 20 tentativas para acertar o número secreto. Boa sorte!')
elif dificuldade == 2:
    tentativas = 10
    print('___________________________________________________________________________')
    print('Você terá 10 tentativas para acertar o número secreto. Boa sorte!')
elif dificuldade == 3:
    tentativas = 5
    print('___________________________________________________________________________')
    print('Você terá 5 tentativas para acertar o número secreto. Boa sorte!')
elif dificuldade != 1 and 2 and 3:
    print('Dificuldade inválida!')
    exit()

while contador < tentativas:
    contador += 1
    print('')
    chute = int(input('Digite um número entre 1 e 100: '))

    if chute < 1 or chute > 100:
        contador -= 1
        print('Número inválido, digite um número de 1 a 100')
    else:
        if chute == numero_secreto:
            print('___________________________________________________________________________')
            print(f'Você acertou!! O número secreto era: {numero_secreto}')
            print(f'Você descobriu o número secreto com {contador} tentativas!')
            break
        elif chute > numero_secreto:
            print(f'Seu chute foi alto, tente novamente ({contador} / {tentativas})')
        else:
            print(f'Seu chute foi baixo, tente novamente ({contador} / {tentativas})')

print('___________________________________________________________________________')            
if contador >= tentativas:
        print(f'Suas tentativas acabaram! O número secreto era: {numero_secreto}')

print('Fim de jogo')
print('___________________________________________________________________________')