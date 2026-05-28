import pygame

pygame.init()

WIDTH = 450
HEIGHT = 520
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3x3 Arrange Puzzle")

font = pygame.font.SysFont(None, 70)
small_font = pygame.font.SysFont(None, 36)

CELL_SIZE = 150

board = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

moves = 0


def draw_board():
    screen.fill((30, 30, 30))

    for row in range(3):
        for col in range(3):
            x = col * CELL_SIZE
            y = row * CELL_SIZE

            pygame.draw.rect(screen, (220, 220, 220),
                             (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, (0, 0, 0),
                             (x, y, CELL_SIZE, CELL_SIZE), 3)

            number = board[row][col]

            if number != 0:
                text = font.render(str(number), True, (0, 0, 0))
                text_rect = text.get_rect(
                    center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2)
                )
                screen.blit(text, text_rect)

    move_text = small_font.render(
        "Moves: " + str(moves), True, (255, 255, 255)
    )
    screen.blit(move_text, (20, 470))


def move(row, col):
    global moves

    for r in range(3):
        for c in range(3):
            if board[r][c] == 0:
                zero_row = r
                zero_col = c

    if (abs(row - zero_row) == 1 and col == zero_col) or \
       (abs(col - zero_col) == 1 and row == zero_row):

        board[zero_row][zero_col], board[row][col] = \
            board[row][col], board[zero_row][zero_col]

        moves += 1


def check_win():
    return board == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]


running = True

while running:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if mouse_y < 450:
                col = mouse_x // CELL_SIZE
                row = mouse_y // CELL_SIZE

                move(row, col)


    draw_board()
    pygame.display.update()

pygame.quit()
