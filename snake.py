import pygame
import random
import sys

# Inicializar pygame
pygame.init()

# Configuración del juego
ancho = 400
alto = 400
retraso = 100  # milisegundos
longitud_inicial = 3

# Crear la ventana de juego
ventana = pygame.display.set_mode((ancho, alto))

# Inicializar la serpiente y la comida
snake_x = ancho // 2
snake_y = alto // 2
snake = [[snake_y, snake_x], [snake_y, snake_x - 10], [snake_y, snake_x - 20]]
food = [random.randint(0, ancho - 10), random.randint(0, alto - 10)]

# Dirección inicial de la serpiente
direccion = [0, -10]

# Bucle principal del juego
while True:
    # Manejar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and direccion!= [0, -10]:
                direccion = [10, 0]
            elif event.key == pygame.K_UP and direccion!= [0, 10]:
                direccion = [-10, 0]
            elif event.key == pygame.K_LEFT and direccion!= [0, 10]:
                direccion = [0, -10]
            elif event.key == pygame.K_RIGHT and direccion!= [0, -10]:
                direccion = [0, 10]

    # Mover la serpiente
    snake.insert(0, [snake[0][0] + direccion[0], snake[0][1] + direccion[1]])

    # Comer la comida
    if snake[0] == food:
        food = [random.randint(0, ancho - 10), random.randint(0, alto - 10)]
    else:
        snake.pop()

    # Dibujar la serpiente y la comida
    ventana.fill((0, 0, 0))
    for s in snake:
        pygame.draw.rect(ventana, (0, 255, 0), (s[1], s[0], 10, 10))
    pygame.draw.rect(ventana, (255, 0, 0), (food[1], food[0], 10, 10))
    pygame.display.update()

    # Verificar colisiones
    if (snake[0][0] < 0 or snake[0][0] >= alto or
        snake[0][1] < 0 or snake[0][1] >= ancho or
        snake[0] in snake[1:]):
        pygame.quit()
        sys.exit()

    # Esperar un poco antes de seguir
    pygame.time.delay(retraso)