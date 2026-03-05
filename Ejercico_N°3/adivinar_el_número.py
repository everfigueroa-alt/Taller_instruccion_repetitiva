import random

número_secreto = random.randint(1, 100)

número = 0

while número != número_secreto:
    número = int(input("Adivina el número 1 y 100: "))


    if número == número_secreto:
        print("¡Acertaste")
    elif número < número_secreto:
        print("Mas alto")
    else:
        print("Mas bajo")
