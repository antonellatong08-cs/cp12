import pygame
import random
import os

pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")

clock = pygame.time.Clock()
FPS = 60

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

bg_file = os.path.join(BASE_PATH, "res", "background2.jpg")
background = pygame.image.load(bg_file)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

DINO_WIDTH = 80
DINO_HEIGHT = 80
OB_WIDTH = 50
OB_HEIGHT = 60

dino_file = os.path.join(BASE_PATH, "res", "spaceship6.png")
dino_img = pygame.image.load(dino_file).convert_alpha()

dino_img.set_colorkey((255, 255, 255))
dino_img = pygame.transform.scale(dino_img, (DINO_WIDTH, DINO_HEIGHT))

ob_file = os.path.join(BASE_PATH, "res", "spaceship4.png")
obstacle_img = pygame.image.load(ob_file).convert_alpha()

obstacle_img.set_colorkey((255, 255, 255))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 30, 30)

GROUND_Y = 320

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)

jump_path = os.path.join(BASE_PATH, "res", "jump.wav")
gameover_path = os.path.join(BASE_PATH, "res", "gameover.wav")
jump_sound = pygame.mixer.Sound(jump_path)
gameover_sound = pygame.mixer.Sound(gameover_path)
jump_sound.set_volume(0.35)
gameover_sound.set_volume(0.45)

menu_bgm_file = os.path.join(BASE_PATH, "res", "bgm.wav")
game_bgm_file = os.path.join(BASE_PATH, "res", "bgm_game.wav")


def draw_text(text, x, y, color=BLACK, big=True):
    if big == True:
        use_font = font
    else:
        use_font = small_font
    text_surface = use_font.render(text, True, color)
    screen.blit(text_surface, (x, y))


def main_menu():
    pygame.mixer.music.load(menu_bgm_file)
    pygame.mixer.music.set_volume(0.18)
    pygame.mixer.music.play(-1)

    while True:
        screen.blit(background, (0, 0))

        draw_text("DINO JUMP", 310, 80)
        draw_text("1 - Play Easy Game", 280, 160, BLACK, False)
        draw_text("2 - Play Hard Game", 280, 200, BLACK, False)
        draw_text("3 - Credits", 280, 240, BLACK, False)
        draw_text("ESC - Quit", 280, 280, BLACK, False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    pygame.mixer.music.stop()
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    pygame.mixer.music.stop()
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    pygame.quit()
                    return

2
def credits():
    while True:
        screen.blit(background, (0, 0))
        draw_text("Credits", 340, 100)
        draw_text("Create by Antonella Tong", 260, 180, BLACK, False)
        draw_text("CS 12 final project", 300, 280, BLACK, False)
        draw_text("Press BACKSPACE to return", 240, 260, BLACK, False)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return


def game_loop(mode):
    pygame.mixer.music.load(game_bgm_file)
    pygame.mixer.music.set_volume(0.18)
    pygame.mixer.music.play(-1)

    dino_x = 100
    dino_y = GROUND_Y - DINO_HEIGHT

    if mode == "easy":
        gravity = 1
        jump_strength = -18
        obstacle_speed = 6
    else:
        gravity = 1.2
        jump_strength = -18
        obstacle_speed = 10

    velocity_y = 0
    jump_count = 0
    max_jump = 2

    obstacle_x = WIDTH
    ob_w = OB_WIDTH
    ob_h = OB_HEIGHT
    obstacle_y = GROUND_Y - ob_h - 40

    score = 0
    running = True
    game_over = False
    is_pause = False

    while running:
        clock.tick(FPS)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p and game_over == False:
                    if is_pause == True:
                        is_pause = False
                        pygame.mixer.music.unpause()
                    else:
                        is_pause = True
                        pygame.mixer.music.pause()
                if event.key == pygame.K_SPACE:
                    if jump_count < max_jump and game_over == False and is_pause == False:
                        velocity_y = jump_strength
                        jump_count = jump_count + 1
                        jump_sound.play()
                if event.key == pygame.K_r and game_over == True:
                    pygame.mixer.music.stop()
                    game_loop(mode)
                    return
                if event.key == pygame.K_BACKSPACE:
                    pygame.mixer.music.stop()
                    main_menu()
                    return

        if is_pause == True:
            draw_text("PAUSED - Press P to continue", 260, 180, RED)
            pygame.display.update()
            continue

        if game_over == False:
            dino_y = dino_y + velocity_y
            velocity_y = velocity_y + gravity

            if dino_y >= GROUND_Y - DINO_HEIGHT:
                dino_y = GROUND_Y - DINO_HEIGHT
                velocity_y = 0
                jump_count = 0

            obstacle_x = obstacle_x - obstacle_speed

            if obstacle_x < -ob_w:
                obstacle_x = WIDTH + random.randint(100, 400)
                ob_w = random.randint(60, 90)
                ob_h = random.randint(70, 100)
                min_gap = 45
                max_gap = 100
                gap = random.randint(min_gap, max_gap)
                obstacle_y = GROUND_Y - ob_h - gap
                score = score + 1

            dino_rect = pygame.Rect(dino_x + 10, dino_y + 10, DINO_WIDTH - 20, DINO_HEIGHT - 20)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, ob_w, ob_h)

            if dino_rect.colliderect(obstacle_rect):
                game_over = True
                gameover_sound.play()
                pygame.mixer.music.pause()

        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)
        scaled_obstacle = pygame.transform.scale(obstacle_img, (ob_w, ob_h))
        screen.blit(dino_img, (dino_x, dino_y))
        screen.blit(scaled_obstacle, (obstacle_x, obstacle_y))

        if mode == "hard":
            text_color = RED
        else:
            text_color = WHITE
        draw_text("Score: " + str(score), 20, 20, BLACK, False)
        draw_text("Mode: " + mode, 20, 50, text_color, False)

        if game_over == True:
            draw_text("GAME OVER", 310, 140)
            draw_text("Press R to restart", 280, 200, BLACK, False)
            draw_text("Press BACKSPACE for menu", 240, 240, BLACK, False)

        pygame.display.update()


main_menu()