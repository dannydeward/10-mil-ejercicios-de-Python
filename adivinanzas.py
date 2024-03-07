import random

def juego_adivinanza(intentos, numero):
    while intentos > 0:
        intento = int(input("Intenta adivinar el número (entre 1 y 100): "))
        if intento < numero:
            print("Demasiado bajo")
        elif intento > numero:
            print("Demasiado alto")
        else:
            print("¡Correcto! ¡Has adivinado el número!")
            break
        intentos -= 1
        if intentos > 0:
            print(f"Te quedan {intentos} intentos")
        else:
            print(f"¡Agotaste tus {intentos_iniciales} intentos! El número era {numero}")

intentos_iniciales = 5
numero_aleatorio = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanzas!")
print("Tienes 5 intentos para adivinar un número entre 1 y 100")

juego_adivinanza(intentos_iniciales, numero_aleatorio)
