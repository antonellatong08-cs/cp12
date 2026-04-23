import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collect Game")

font = pygame.font.SysFont(None, 36)

x, y = 400, 300
player_size = 30
speed = 5
color = (255, 255, 255)

target_size = 30

def get_next_position(size):
    return random.randint(0, WIDTH - size), random.randint(0, HEIGHT - size)

x1, y1 = get_next_position(target_size)

score = 0

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed

    if x >= WIDTH:
        x = -player_size
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif x <= -player_size:
        x = WIDTH
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    if y >= HEIGHT:
        y = -player_size
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    elif y <= -player_size:
        y = HEIGHT
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    player = pygame.Rect(x, y, player_size, player_size)
    target = pygame.Rect(x1, y1, target_size, target_size)

    if player.colliderect(target):
        score += 1

        target_size = max(10, target_size - 2)

        x1, y1 = get_next_position(target_size)

        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))

    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, color, player)
    pygame.draw.rect(screen, (255, 0, 0), target)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()