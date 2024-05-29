import random

# Solicitar una palabra al usuario
palabras = ['python', 'programacion', 'computadora', 'juego', 'ahorcado']
palabra_secreta = random.choice(palabras)
palabra_clave = '*' * len(palabra_secreta)

# Inicializar variables
longitud_palabra = len(palabra_secreta)
letras_descubiertas = ['_'] * longitud_palabra
vidas = 7

# Bucle principal del juego
while vidas > 0 and '_' in letras_descubiertas:
    # Imprimir el estado actual del juego
    print('Palabra secreta:', palabra_clave)
    print('Palabra descubierta:', ' '.join(letras_descubiertas))
    print('Vidas restantes:', vidas)

    # Solicitar una letra al usuario
    letra = input('Ingresa una letra: ').lower()

    # Verificar si la letra está en la palabra secreta
    if letra in palabra_secreta:
        # Actualizar las letras descubiertas
        for i in range(longitud_palabra):
            if palabra_secreta[i] == letra:
                letras_descubiertas[i] = letra
                # Actualizar la palabra clave
                palabra_clave = palabra_clave[:i] + letra + palabra_clave[i+1:]
    else:
        # Restar una vida
        vidas -= 1

# Imprimir el resultado final
if '_' in letras_descubiertas:
    print('Perdiste! La palabra secreta era', palabra_secreta)
else:
    print('Ganaste! La palabra secreta era', palabra_secreta)