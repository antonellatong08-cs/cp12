import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker")

background = pygame.image.load("res\\background.jpg")
screen.blit(background, (0, 0))

spaceship = pygame.image.load("res\\spaceship.jpg")
spaceship = pygame.transform.scale(spaceship, (100, 100))

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

circle_x = 400
circle_y = 300
circle_radius = 50
score = 0
MIN_radius = 10
small = 3

message = ""
show_time = 0
DISPLAY_DURATION = 500

total_time = 10
time_left = total_time
game_over = False

def draw_circle(x, y, radius):
    #circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    screen.blit(spaceship, (x-radius , y-radius))
    #pygame.draw.circle(screen, (x, y), radius)

def draw_info(time_left, points):
    time_text = font.render(f"Time: {time_left}", True, (255, 255, 0))
    score_text = font.render(f"Score: {points}", True, (255, 255, 255))
    screen.blit(time_text, (20, 20))
    screen.blit(score_text, (180, 20))

def draw_message(text):
    if text:
        msg_surface = font.render(text, True, (0, 255, 255))
        screen.blit(msg_surface, (20, 70))

def is_inside_circle(mouse_x, mouse_y, cx, cy, r):
    dx = mouse_x - cx
    dy = mouse_y - cy
    return dx*dx + dy*dy <= r*r

def get_next_circle_position(r):
    new_x = random.randint(r, WIDTH - r)
    new_y = random.randint(r, HEIGHT - r)
    return new_x, new_y

running = True

while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, circle_radius):
                score += 1
                circle_x, circle_y = get_next_circle_position(circle_radius)
                if circle_radius > MIN_radius:
                    circle_radius -= small
                message = random.choice(["Good", "Great", "Nice", "Perfect", "Excellent", "Well Done"])
                time_left = total_time
            else:
                score = max(score - 1, 0)
                message = "Try Again"
            show_time = current_time

    if not game_over:
        time_left -= 1 / 60
        if time_left <= 0:
            time_left = 0
            game_over = True

    screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))

    if current_time - show_time > DISPLAY_DURATION:
        message = ""

    draw_circle(circle_x, circle_y, circle_radius)
    draw_info(int(time_left), score)
    draw_message(message)

    if game_over:
        go_text = font.render("Game Over!", True, (255, 0, 0))
        screen.blit(go_text, (WIDTH//2 - 80, HEIGHT//2))

    pygame.display.update()
    clock.tick(60)

pygame.quit()