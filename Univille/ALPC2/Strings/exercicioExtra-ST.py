frase = 'O rato roeu a rica roupa do rei da russia'

pos = -1
while True:
    pos = frase.find('r', pos + 1)
    if pos > -1:
        print(pos)
    else:
        break