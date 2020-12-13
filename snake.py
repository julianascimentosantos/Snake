import pygame, random
from pygame.locals import *

# Tornar o grid da maçã 10 igual o da cobra para alinhar
def on_grid_random():
    x = random.randint(0,590)
    y = random.randint(0,590)
    return(x//10 * 10, y//10 * 10)

# Testar a colisão:
def collision(c1, c2):
    return(c1[0] == c2[0]) and (c1[1] == c2[1])

# Criando as direções
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()

# Objeto de tela
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake')

# Criando a cobra
snake = [(200, 200), (210, 200), (220,200)] # é uma continuação 200 > 210 > 220 (para a direita), e permanece 200 para baixo

# Especificações da cobra
snake_skin = pygame.Surface((10, 10))
snake_skin.fill((255, 255, 255))

# Criando a maçã
apple = pygame.Surface((10, 10))
apple.fill((255, 0, 0))

# Gerar uma posição aleatória para a maçã
apple_pos = on_grid_random()

# Direção da cobra inicialmente
my_direction = LEFT

# Para controlar o tempo da cobra
clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        
        # Para sair do jogo
        if event.type == QUIT:
            pygame.quit()

        # Para controlar a cobra
        if event.type == KEYDOWN:
            if event.key == K_UP:
                my_direction = UP
            if event.key == K_DOWN:
                my_direction = DOWN
            if event.key == K_LEFT:
                my_direction = LEFT
            if event.key == K_RIGHT:
                my_direction = RIGHT

    # Momento da colisão com a maçã   
    if collision(snake[0], apple_pos):
        apple_pos = on_grid_random()
        snake.append((0,0))

    # Momento da colisão com a cobra   
    if collision(snake[0], snake[0:]):
        print('Game Over')
        pygame.quit()

    # Para movimentar o corpo da cobra
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    # Para movimentar a cabeça da cobra (x(lados), y(cima e baixo))
    if my_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)

    if my_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)

    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])

    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])        

    # Para limpar o jogo antes de começar
    screen.fill((0, 0, 0))

    # Para plotar a maçã:
    screen.blit(apple, apple_pos)

    for pos in snake:
        # Para plotar o jogo na tela
        screen.blit(snake_skin, pos)

    pygame.display.update()