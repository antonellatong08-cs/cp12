import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker")

font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

circle_x = 400
circle_y = 300
circle_radius = 50
score = 0
MIN_radius= 10
small = 3

def draw_circle(x, y, radius):
    circle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    pygame.draw.circle(screen, circle_color, (x, y), radius)



def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))


def is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, radius):
    dx = mouse_x - circle_x
    dy = mouse_y - circle_y
    return dx * dx + dy * dy <= radius * radius


def get_next_circle_position(x, y):
    new_x = random.randint(circle_radius, WIDTH - circle_radius)
    new_y = random.randint(circle_radius, HEIGHT - circle_radius)
    return new_x, new_y


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, circle_radius):
                score = score + 1
                circle_x, circle_y = get_next_circle_position(circle_x, circle_y)
                if circle_radius > MIN_radius:
                    circle_radius = circle_radius - small
    screen.fill((30, 30, 30))
    draw_circle(circle_x, circle_y, circle_radius)
    draw_score(score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()