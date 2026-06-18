import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump Starter")

clock = pygame.time.Clock()
FPS = 60

background = pygame.image.load("res/background2.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
finish_bg = pygame.image.load("res/finish.jpg")
finish_bg = pygame.transform.scale(finish_bg, (WIDTH, HEIGHT))

DINO_WIDTH, DINO_HEIGHT = 80, 80
OB_WIDTH, OB_HEIGHT = 50, 60
BONUS_SIZE = 70

dino_img = pygame.image.load("res/spaceship6.png").convert_alpha()
dino_img = pygame.transform.scale(dino_img, (DINO_WIDTH, DINO_HEIGHT))

obstacle_img = pygame.image.load("res/spaceship4.png").convert_alpha()
obstacle_img = pygame.transform.scale(obstacle_img, (OB_WIDTH, OB_HEIGHT))

bonus_img = pygame.image.load("res/bonus.png").convert_alpha()
bonus_img = pygame.transform.scale(bonus_img, (BONUS_SIZE, BONUS_SIZE))

jump_sound = pygame.mixer.Sound("res/sound 3.mp3")
gameover_sound = pygame.mixer.Sound("res/gameover.wav")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)

GROUND_Y = 320

font = pygame.font.SysFont(None, 40)
small_font = pygame.font.SysFont(None, 28)

WIN_SCORE = 5
debug_invincible = False


def draw_text(text, x, y, color=BLACK, big=True):
    used_font = font if big else small_font
    img = used_font.render(text, True, color)
    screen.blit(img, (x, y))


def main_menu():
    global debug_invincible
    pygame.mixer.music.load("res/bgm.wav")
    pygame.mixer.music.play(-1)
    while True:
        screen.blit(background, (0, 0))
        draw_text("DINO JUMP", 310, 80)
        draw_text("1 - Play Easy Game", 280, 160, big=False)
        draw_text("2 - Play Hard Game", 280, 200, big=False)
        draw_text("3 - Credits", 280, 240, big=False)
        draw_text("ESC - Quit", 280, 280, big=False)
        if debug_invincible:
            draw_text("DEBUG MODE ACTIVE", 300, 320, RED, big=False)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_EQUALS or event.key == pygame.K_KP_PLUS:
                    debug_invincible = not debug_invincible
                elif event.key == pygame.K_1:
                    pygame.mixer.music.stop()
                    game_loop("easy")
                elif event.key == pygame.K_2:
                    pygame.mixer.music.stop()
                    game_loop("hard")
                elif event.key == pygame.K_3:
                    credits()
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return


def credits():
    while True:
        screen.blit(background, (0, 0))
        draw_text("Credits", 340, 100)
        draw_text("Created by Antonella Tong", 260, 180, big=False)
        draw_text("Press BACKSPACE to return", 240, 260, big=False)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    return


def game_loop(mode):
    global debug_invincible
    pygame.mixer.music.load("res/bgm_game.wav")
    pygame.mixer.music.play(-1)
    dino_x = 100
    dino_y = GROUND_Y - DINO_HEIGHT
    auto_jump_timer = 0
    if mode == "easy":
        gravity = 1
        jump_strength = -18
        obstacle_speed = 6
    else:
        gravity = 1.2
        jump_strength = -18
        obstacle_speed = 9
    velocity_y = 0
    jump_count = 0
    on_ground = True
    obstacle_x = WIDTH
    obstacle_y = GROUND_Y - OB_HEIGHT
    bonus_x = WIDTH
    bonus_y = random.randint(40, 180)
    bonus_active = False
    last_bonus_time = time.time()
    bonus_interval = 20
    invincible = False
    invincible_start = 0
    invincible_time = 5
    flash_gap = 0.25
    show_dino = True
    score = 0
    running = True
    game_over = False
    game_win = False
    target_win = 10
    if debug_invincible == False:
        target_win = WIN_SCORE
    while running:
        now = time.time()
        clock.tick(FPS)
        if game_win:
            screen.blit(finish_bg, (0, 0))
        else:
            screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_over == False and game_win == False:
                    if jump_count < 2:
                        velocity_y = jump_strength
                        jump_count = jump_count + 1
                        jump_sound.play()
                if event.key == pygame.K_r and (game_over or game_win):
                    pygame.mixer.music.stop()
                    return game_loop(mode)
                if event.key == pygame.K_BACKSPACE:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("res/bgm.wav")
                    pygame.mixer.music.play(-1)
                    return
        if game_over == False and game_win == False:
            dino_y = dino_y + velocity_y
            velocity_y = velocity_y + gravity
            if dino_y >= GROUND_Y - DINO_HEIGHT:
                dino_y = GROUND_Y - DINO_HEIGHT
                velocity_y = 0
                on_ground = True
                jump_count = 0
            obstacle_x = obstacle_x - obstacle_speed
            if obstacle_x < -OB_WIDTH:
                obstacle_x = WIDTH + random.randint(100, 400)
                score = score + 1
            if bonus_active == False:
                if now - last_bonus_time >= bonus_interval:
                    bonus_active = True
                    bonus_x = WIDTH
                    bonus_y = random.randint(40, 180)
                    last_bonus_time = now
            else:
                bonus_x = bonus_x - obstacle_speed
                if bonus_x < -BONUS_SIZE:
                    bonus_active = False
            dino_rect = pygame.Rect(dino_x, dino_y, DINO_WIDTH, DINO_HEIGHT)
            obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, OB_WIDTH, OB_HEIGHT)
            if bonus_active:
                bonus_rect = pygame.Rect(bonus_x, bonus_y, BONUS_SIZE, BONUS_SIZE)
                if dino_rect.colliderect(bonus_rect):
                    bonus_active = False
                    invincible = True
                    invincible_start = now
            if debug_invincible:
                show_dino = True
            else:
                if invincible:
                    if now - invincible_start >= invincible_time:
                        invincible = False
                    flash_cycle = int((now - invincible_start) / flash_gap)
                    if flash_cycle % 2 == 0:
                        show_dino = True
                    else:
                        show_dino = False
                else:
                    show_dino = True
                    if dino_rect.colliderect(obstacle_rect):
                        game_over = True
                        gameover_sound.play()
            if score >= target_win:
                game_win = True
        else:
            if game_win:
                auto_jump_timer = auto_jump_timer + clock.tick() / 1000
                if auto_jump_timer > 0.8:
                    velocity_y = jump_strength
                    auto_jump_timer = 0
                dino_y = dino_y + velocity_y
                velocity_y = velocity_y + gravity
                if dino_y >= GROUND_Y - DINO_HEIGHT:
                    dino_y = GROUND_Y - DINO_HEIGHT
                    velocity_y = 0
        pygame.draw.line(screen, BLACK, (0, GROUND_Y), (WIDTH, GROUND_Y), 3)
        if game_win == False:
            screen.blit(obstacle_img, (obstacle_x, obstacle_y))
            if bonus_active:
                screen.blit(bonus_img, (bonus_x, bonus_y))
        if show_dino:
            screen.blit(dino_img, (dino_x, dino_y))
        if game_win:
            screen.blit(bonus_img, (dino_x - BONUS_SIZE + 30, dino_y))
        text_color = BLACK
        if game_win:
            text_color = WHITE
        draw_text("Score: " + str(score), 20, 20, text_color, big=False)
        draw_text("Mode: " + mode, 20, 50, text_color, big=False)
        if invincible and debug_invincible == False:
            remain = int(invincible_time - (now - invincible_start))
            draw_text("Invincible:" + str(remain) + "s", 20, 80, RED, big=False)
        if debug_invincible:
            draw_text("DEBUG INVINCIBLE ON", 20, 110, RED, big=False)
        if game_over:
            draw_text("GAME OVER", 310, 140)
            draw_text("Press R to restart", 280, 200, big=False)
            draw_text("Press BACKSPACE for menu", 240, 240, big=False)
        if game_win:
            draw_text("YOU WIN!", 320, 140, WHITE)
            draw_text("Press R to play again", 270, 200, WHITE, big=False)
            draw_text("Press BACKSPACE for menu", 240, 240, WHITE, big=False)
        pygame.display.update()


main_menu()