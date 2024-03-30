"""Игра крестики - нолики в терминале."""
from gameparts import Board
from gameparts.exceptions import CellOccupiedError, FieldIndexError


def save_result(result: str) -> None:
    """Сохраняет результат игры в файл 'result.txt'."""
    with open('results.txt', 'a') as f:
        f.write(result + '\n')


def main() -> None:
    """Основной цикл игры."""
    game = Board()
    current_player: str = 'X'
    running: bool = True
    game.display()

    while running:

        print(f'Ход делают {current_player}')

        while True:
            try:
                row: int = int(input('Введите номер строки: '))
                if row < 0 or row >= game.field_size:
                    raise FieldIndexError
                column: int = int(input('Введите номер столбца: '))
                if column < 0 or column >= game.field_size:
                    raise FieldIndexError
                if game.board[row][column] != ' ':
                    raise CellOccupiedError
            except ValueError:
                print(
                    'Буквы вводить нельзя. Только числа. '
                    'Пожалуйста, введите значение для строки и столбца заново'
                )
                continue
            except FieldIndexError:
                print(
                    f'Значение должно быть неотрицательным и меньше '
                    f'{game.field_size}.'
                )
                print('Введите значение для строки столбца заново.')
                continue
            except CellOccupiedError:
                print('Ячейка занята.')
                print('Введите другие координаты.')
                continue
            except Exception as e:
                print(f'Возникла ошибка: {e}')
            else:
                break

        game.make_move(row, column, current_player)
        game.display()
        if game.check_win(current_player):
            winner: str = f'Победители {current_player}!'
            print(winner)
            save_result(winner)
            running: bool = False
        elif game.is_board_full():
            nobody: str = 'Ничья'
            print(nobody)
            save_result(nobody)
            running: bool = False

        current_player = 'O' if current_player == 'X' else 'X'


if __name__ == '__main__':
    main()
