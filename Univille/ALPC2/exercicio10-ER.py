""" 
10. Anacleto tem 1,50m e cresce 2 centímetros por ano, enquanto Felisberto 
tem 1,10m e cresce 3 centímetros por ano. Construa um programa que calcule 
e apresente quantos anos serão necessários para que Felisberto seja maior que Anacleto.
 """

anacleto = 1.50
felisberto = 1.10
anos = 0


while True:
    if anacleto < felisberto:
        break
    else:
        anos = anos + 1
        anacleto = anacleto + 0.02
        print(f"Anacleto está com {anacleto:.2f}")
        felisberto = felisberto + 0.03
        print(f"Felisberto está com {felisberto:.2f}")
        print("")
print(f"Felisberto ficou maior que Anacleto depois de {anos} anos.")


