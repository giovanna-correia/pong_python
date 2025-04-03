import pygame
import random

# Inicialização do pygame
pygame.init()

# Configurações da tela
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Configurações da bola
ball = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

# Configurações das raquetes
paddle_width, paddle_height = 10, 100
paddle1 = pygame.Rect(20, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
paddle2 = pygame.Rect(WIDTH - 30, HEIGHT//2 - paddle_height//2, paddle_width, paddle_height)
paddle_speed = 5

# Pontuação
score1, score2 = 0, 0

def save_score():
    with open("pontuacoes.txt", "a") as f:
        f.write(f"{score1} - {score2}\n")

# Loop do jogo
running = True
clock = pygame.time.Clock()
while running:
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, paddle1)
    pygame.draw.rect(screen, WHITE, paddle2)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_score()
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.top > 0:
        paddle1.y -= paddle_speed
    if keys[pygame.K_s] and paddle1.bottom < HEIGHT:
        paddle1.y += paddle_speed
    if keys[pygame.K_UP] and paddle2.top > 0:
        paddle2.y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2.bottom < HEIGHT:
        paddle2.y += paddle_speed

    # Movimento da bola
    ball.x += ball_dx
    ball.y += ball_dy

    # Colisão com paredes
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Colisão com raquetes
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_dx = -ball_dx

    # Pontuação
    if ball.left <= 0:
        score2 += 1
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])
    if ball.right >= WIDTH:
        score1 += 1
        ball.x, ball.y = WIDTH//2 - 15, HEIGHT//2 - 15
        ball_dx, ball_dy = random.choice([-4, 4]), random.choice([-4, 4])

    # Exibir pontuação
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score1} - {score2}", True, WHITE)
    screen.blit(text, (WIDTH//2 - 30, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
