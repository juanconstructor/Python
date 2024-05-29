import random
import string

# Definir las constantes de cadena
letras = string.ascii_letters
digitos = string.digits

# Definir el alfabeto
alfabeto = letras + digitos

# Generar la contraseña
pwd = ''.join(random.choice(alfabeto) for _ in range(10))

# Verificar si la contraseña cumple las restricciones
while True:
    if (any(char.isdigit() for char in pwd) and 
        any(char.isalpha() for char in pwd)):
        break
    pwd = ''.join(random.choice(alfabeto) for _ in range(10))

# Mostrar la contraseña generada
print(f"La contraseña generada es: {pwd}")