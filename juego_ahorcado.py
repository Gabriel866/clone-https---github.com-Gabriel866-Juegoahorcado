import random

def obtener_palabra_aleatoria(palabra_anterior=None):
    palabras = ["perro", "gato", "codigo", "software"]
    palabra_aleatoria = random.choice(palabras)
    while palabra_aleatoria == palabra_anterior:
        palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero += "_"
    print(tablero)

def jugar_ahorcado(palabra_anterior=None):
    palabra_secreta = obtener_palabra_aleatoria(palabra_anterior)
    letras_adivinadas = []
    intentos_restantes = 6

    while intentos_restantes > 0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        letra = input("Introduce una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has introducido esa letra. Prueba otra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            if set(palabra_secreta).issubset(set(letras_adivinadas)):
                print("¡Felicidades, has acertado la palabra!")
                mostrar_tablero(palabra_secreta, letras_adivinadas)
                break
        else:
            intentos_restantes -= 1
            print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")

    if intentos_restantes == 0:
        print(f"Has perdido. La palabra secreta era: {palabra_secreta}")
    
    return palabra_secreta  # Para poder compararla después

# Bucle para jugar varias veces
palabra_anterior = None
while True:
    palabra_anterior = jugar_ahorcado(palabra_anterior)
    respuesta = input("¿Quieres jugar otra vez? (s/n): ").lower()
    if respuesta != "s":
        print("¡Gracias por jugar! Hasta la próxima.")
        break



