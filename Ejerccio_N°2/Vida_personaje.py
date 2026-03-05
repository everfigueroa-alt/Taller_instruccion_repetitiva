import random

vida = 50

while vida > 0:
    daño = random.randint(1, 15)
    vida = vida - daño

    print("El jefe te quto:", daño)
    print("Vida que te queda:", vida)

if vida <= 0:
    print("Perdiste")
breakpoint