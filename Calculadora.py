# Calculadora básica en Python

def suma(num1, num2):
  return num1 + num2

def resta(num1, num2):
  return num1 - num2

def multiplicacion(num1, num2):
  return num1 * num2

def division(num1, num2):
  if num2 != 0:
    return num1 / num2
  else:
    return "Error: no se puede dividir entre cero"

print("Calculadora básica")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")

while True:
  opcion = int(input("Ingrese la opción deseada: "))

  if opcion == 5:
    break

  num1 = float(input("Ingrese el primer número: "))
  num2 = float(input("Ingrese el segundo número: "))

  if opcion == 1:
    resultado = suma(num1, num2)
  elif opcion == 2:
    resultado = resta(num1, num2)
  elif opcion == 3:
    resultado = multiplicacion(num1, num2)
  elif opcion == 4:
    resultado = division(num1, num2)

  print("El resultado es:", resultado)