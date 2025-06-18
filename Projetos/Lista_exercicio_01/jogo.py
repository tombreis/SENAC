import pygame
import sys

# Inicialização
pygame.init()

# Tamanho da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Plataforma - Estilo Dangerous Dave")

# Cores
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
BLACK = (0, 0, 0)

# Jogador
player_width, player_height = 40, 60
player_x, player_y = 100, HEIGHT - 150
player_vel_x = 0
player_vel_y = 0
jumping = False

# Física
gravity = 1
jump_strength = -15
move_speed = 5

# Plataforma
platform = pygame.Rect(0, HEIGHT - 80, WIDTH, 40)

# Relógio
clock = pygame.time.Clock()

# Game loop
while True:
    screen.fill(BLACK)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas pressionadas
    keys = pygame.key.get_pressed()
    player_vel_x = 0
    if keys[pygame.K_LEFT]:
        player_vel_x = -move_speed
    if keys[pygame.K_RIGHT]:
        player_vel_x = move_speed
    if keys[pygame.K_SPACE]:
        if not jumping:
            player_vel_y = jump_strength
            jumping = True

    # Atualiza posição
    player_x += player_vel_x
    player_y += player_vel_y
    player_vel_y += gravity

    # Colisão com plataforma
    if player_y + player_height >= platform.top:
        player_y = platform.top - player_height
        player_vel_y = 0
        jumping = False

    # Desenhar plataforma
    pygame.draw.rect(screen, GREEN, platform)

    # Desenhar jogador
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))

    pygame.display.flip()
    clock.tick(60)
