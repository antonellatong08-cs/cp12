import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")

clock = pygame.time.Clock()
FPS = 60

# ---------------- IMAGES ----------------
background = pygame.image.load("res/background2.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

DINO_WIDTH, DINO_HEIGHT = 60, 80
OB_WIDTH, OB_HEIGHT = 50, 60

dino_img = pygame.image.load("res/spaceship1.png").convert_alpha()
dino_img = pygame.transform.scale(dino_img, (DINO_WIDTH, DINO_HEIGHT))

obstacle_img = pygame.image.load("res/spaceship4.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (OB_WIDTH, OB_HEIGHT))

# ---------------- COLORS ----------------
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ---------------- GAME SETTINGS ----------------
GROUND_Y = 320

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)


def draw_text(text, x, y, color=BLACK, big=True):
    used_font = font if big else small_font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


# ---------------- MENU ----------------
def main_menu():
    while True:
        screen.blit(background, (0, 0))

        draw_text("DINO JUMP", 310, 80)
        draw_text("1 - Play Easy Game", 280, 160, big=False)
        draw_text("2 - Play Hard Game", 280, 200, big=False)
        draw_text("3 - Credits", 280, 240, big=False)
        draw_text("ESC - Quit", 280, 280, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


# ---------------- CREDITS ----------------
def credits():
    while True:
        screen.blit(background, (0, 0))

        draw_text("Credits", 340, 100)
        draw_text("Created by Students", 260, 180, big=False)
        draw_text("Press BACKSPACE to return", 240, 260, big=False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return


# ---------------- GAME ----------------
def game_loop(mode):
    dino_x = 100
    dino_y = GROUND_Y - DINO_HEIGHT

    velocity_y = 0
    gravity = 1
    jump_strength = -18
    on_ground = True

    obstacle_x = WIDTH
    obstacle_y = GROUND_Y - OB_HEIGHT

    obstacle_speed = 6 if mode == "easy" else 9

    score = 0
    running = True
    game_over = False

    while running:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and on_ground and not game_over:
                    velocity_y = jump_strength
                    on_ground = False

                if event.key == pygame.K_r and game_over:
                    return game_loop(mode)

                if event.key == pygame.K_BACKSPACE:
                    return

        if not game_over:

            # --------- DINO PHYSICS ----------
            dino_y += velocity_y
            velocity_y += gravity

            if dino_y >= GROUND_Y - DINO_HEIGHT:
                dino_y = GROUND_Y - DINO_HEIGHT
                velocity_y = 0
                on_ground = True

            # --------- OBSTACLE ----------
            obstacle_x -= obstacle_speed

            if obstacle_x < -OB_WIDTH:
                obstacle_x = WIDTH + random.randint(100, 400)
                score += 1

            # --------- COLLISION ----------
            dino_rect = pygame.Rect(dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OB_WIDTH, OB_HEIGHT)

            if dino_rect.colliderect(obstacle_rect):
                game_over = True

        # --------- DRAW ----------
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)

        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(obstacle_img, (obstacle_x, obstacle_y))

        draw_text("Score: " + str(score), 20, 20, big=False)
        draw_text("Mode: " + mode, 20, 50, big=False)

        if game_over:
            draw_text("GAME OVER", 310, 140)
            draw_text("Press R to restart", 280, 200, big=False)
            draw_text("Press BACKSPACE for menu", 240, 240, big=False)

        pygame.display.update()


main_menu()