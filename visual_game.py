"""Крестики - нолики."""
import pygame
from gameparts import Board

pygame.init()

# Здесь определены разные константы, например,
# размер ячейки и доски, цвет и толщина линий.
# Эти константы используются при отрисовке графики.
CELL_SIZE = 100
BOARD_SIZE = 3
WIDTH = HEIGHT = CELL_SIZE * BOARD_SIZE
LINE_WIDTH = 15
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
X_COLOR = (84, 84, 84)
O_COLOR = (242, 235, 211)
X_WIDTH = 15
O_WIDTH = 15
SPACE = CELL_SIZE // 4

# Настройка экрана.
# Размер графического окна для игрового поля.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Заголовок окна.
pygame.display.set_caption('Крестики-нолики')
# Фон окна с заданным цветом.
screen.fill(BG_COLOR)


def draw_lines() -> None:
    """Функция отвечает за отрисовку горизонтальных и вертикальных линий."""
    # Горизонтальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * CELL_SIZE),
            (WIDTH, i * CELL_SIZE),
            LINE_WIDTH
        )
    # Вертикальные линии.
    for i in range(1, BOARD_SIZE):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * CELL_SIZE, 0),
            (i * CELL_SIZE, HEIGHT),
            LINE_WIDTH
        )


def draw_figures(board) -> None:
    """Функция отвечает за отрисовку фигур на доске."""
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row][col] == 'X':
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (col * CELL_SIZE + SPACE, row * CELL_SIZE + SPACE),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    X_WIDTH
                )
                pygame.draw.line(
                    screen,
                    X_COLOR,
                    (
                        col * CELL_SIZE + SPACE,
                        row * CELL_SIZE + CELL_SIZE - SPACE
                    ),
                    (
                        col * CELL_SIZE + CELL_SIZE - SPACE,
                        row * CELL_SIZE + SPACE
                    ),
                    X_WIDTH
                )
            elif board[row][col] == 'O':
                pygame.draw.circle(
                    screen,
                    O_COLOR,
                    (
                        col * CELL_SIZE + CELL_SIZE // 2,
                        row * CELL_SIZE + CELL_SIZE // 2
                    ),
                    CELL_SIZE // 2 - SPACE,
                    O_WIDTH
                )


def save_result(result: str) -> None:
    """Функция сохраняет результат игры в файл 'result.txt'."""
    with open('results.txt', 'a') as f:
        f.write(result + '\n')


def main() -> None:
    """Функция запускается игровой цикл."""
    game = Board()
    # Первым ходить крестик.
    current_player: str = 'X'
    running: bool = True
    draw_lines()

    # В цикле обрабатываются такие события, как
    # нажатие кнопок мыши и закрытие окна.
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running: bool = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_y = event.pos[0]
                mouse_x = event.pos[1]
                clicked_row = mouse_x // CELL_SIZE
                clicked_col = mouse_y // CELL_SIZE
                # Если ячейка свободна : сделать ход,
                if game.board[clicked_row][clicked_col] == ' ':
                    game.make_move(clicked_row, clicked_col, current_player)
                    # проверить на победу,
                    if game.check_win(current_player):
                        winner: str = f'Победители {current_player}!'
                        print(winner)
                        save_result(winner)
                        running: bool = False
                    # проверить на ничью,
                    elif game.is_board_full():
                        nobody: str = 'Ничья'
                        print(nobody)
                        save_result(nobody)
                        running: bool = False
                    # сменить игрока.
                    current_player = 'O' if current_player == 'X' else 'X'
                    draw_figures(game.board)

        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
