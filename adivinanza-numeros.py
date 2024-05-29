import random

def get_number():
    while True:
        try:
            number = int(input("Ingresa un número: "))
            return number
        except ValueError:
            print("Por favor, ingresa un número entero.")

def get_score():
    try:
        with open("scores.txt", "r") as file:
            scores = file.read().splitlines()
            return scores
    except FileNotFoundError:
        return []

def update_scores(score):
    scores = get_score()
    scores.append(score)
    with open("scores.txt", "w") as file:
        for score in scores:
            file.write(f"{score}\n")

def show_scores():
    scores = get_score()
    if not scores:
        print("No hay puntajes registrados.")
    else:
        print("Los mejores puntajes son:")
        for i, score in enumerate(sorted(scores, reverse=True)):
            print(f"{i+1}. {score}")

def play_game():
    print("Bienvenido al juego de adivinanzas de números!")
    customize = input("¿Deseas personalizar los números? (s/n): ").lower()
    if customize == "s":
        min_number = int(input("Ingresa el número mínimo: "))
        max_number = int(input("Ingresa el número máximo: "))
        if min_number > max_number:
            print("El número mínimo debe ser menor que el número máximo.")
            return
        number_to_guess = random.randint(min_number, max_number)
    else:
        number_to_guess = random.randint(1, 100)
    attempts = 0
    while True:
        guess = get_number()
        attempts += 1
        if guess < number_to_guess:
            print("El número es demasiado bajo.")
        elif guess > number_to_guess:
            print("El número es demasiado alto.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {attempts} intentos.")
            score = attempts
            update_scores(score)
            show_scores()
            break
        if attempts == 10:
            print("Lo siento, has agotado tus intentos.")
            name = input("Por favor, ingresa tu nombre para guardar tu puntaje: ")
            score = f"{name}: {attempts}"
            update_scores(score)
            show_scores()
            break

if __name__ == "__main__":
    play_game()