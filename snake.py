import pygame, random
from pygame.locals import *

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
apple_pos = (random.randint(0, 590), random.randint(0, 590))

# Direção da cobra inicialmente
my_direction = LEFT

while True:

    for event in pygame.event.get():
        
        # Para sair do jogo
        if event.type == QUIT:
            pygame.quit()

    # Para limpar o jogo antes de começar
    screen.fill((0, 0, 0))

    # Para plotar a maçã:
    screen.blit(apple, apple_pos)

    for pos in snake:
        # Para plotar o jogo na tela
        screen.blit(snake_skin, pos)

    pygame.display.update()