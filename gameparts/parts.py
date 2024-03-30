"""Модуль, импортируется для игры в терминале и через инициализацию pygame."""


class Board:
    """Класс содержит методы, обрабатывающие действия и события в игре."""

    field_size: int = 3

    def __init__(self):
        """Конструктор класса. Содержит атрибут объетка - игровое поле."""
        self.board: list[list[str]] = [
            [' ' for _ in range(self.field_size)]
            for _ in range(self.field_size)
            ]

    def make_move(self, row: int, col: int, player: str) -> None:
        """Функция заменяет пустые клетки игровой доски (списка) на фигуру."""
        self.board[row][col] = player

    def display(self) -> None:
        """Метод используется для отрисовки игрового поля."""
        for row in self.board:
            print(' | '.join(row))
            print('-' * 10)

    def is_board_full(self) -> bool:
        """Проверяет, что игровое поле заполнено фигурами."""
        for i in range(self.field_size):
            for j in range(self.field_size):
                if self.board[i][j] == ' ':
                    return False
        return True

    def check_win(self, player: str) -> bool:
        """Проверяет на заполненность горизонталей, вертикалей, диагоналей."""
        for i in range(3):
            if (all([self.board[i][j] == player for j in range(3)]) or
               all([self.board[j][i] == player for j in range(3)])):
                return True
        if (
            self.board[0][0] == self.board[1][1] == self.board[2][2] == player
            or
            self.board[0][2] == self.board[1][1] == self.board[2][0] == player
        ):
            return True
        return False
