from typing import Literal

# Тип для символів на сітці
CROSS = "X"
ZERO = "O"
Symbol = Literal["X", "O"]
Cell = Literal["X", "O", " "]  # " " — порожня клітинка


def create_grid(size: int = 3) -> list[list[Cell]]:
    """
    Створює і повертає порожню сітку для гри «Хрестики-нулики».

    :param size: int - Розмір квадратної сітки (типово 3x3)
    :return: list[list[Cell]] - Двовимірний список, що представляє ігрове поле.
             Кожна клітинка містить "X", "O" або " " (пробіл для порожньої).
    """
    # TODO: створити список списків розміром size x size, заповнений пробілами " "

    grid = []

    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(" ")
        grid.append(row)

    return grid


def print_grid(grid: list[list[Cell]]) -> None:
    """
    Виводить поточний стан сітки на екран у зручному для читання вигляді.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: None
    """
    # TODO: красиво вивести сітку, наприклад:
    #  X | O |
    # ---+---+---
    #    | X | O
    # ---+---+---
    #  O |   | X

    for row in grid:
        print(" | ".join(row))
        print("---+---+---")


def add_symbol_to_grid(
    grid: list[list[Cell]], row: int, col: int, symbol: Symbol
) -> bool:
    """
    Додає новий символ на сітку за вказаними координатами.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :param row: int - Індекс рядка (0-based).
    :param col: int - Індекс стовпчика (0-based).
    :param symbol: Symbol - Символ гравця ("X" або "O").
    :return: bool - True, якщо хід успішний (клітинка була вільна),
                    False, якщо клітинка вже зайнята або координати некоректні.
    """
    # TODO:
    # 1. Перевірити, що row і col в межах розміру сітки.
    # 2. Перевірити, що в цій клітинці зараз " " (порожньо).
    # 3. Якщо все ок — записати symbol у grid[row][col] і повернути True.
    # 4. Інакше повернути False.
    size = len(grid)
    if row < 0 or row >= size or col < 0 or col >= size:
        return False

    if grid[row][col] != " ":
        return False

    grid[row][col] = symbol
    return True


def ask_user_move(player_name: str, grid: list[list[Cell]]) -> tuple[int, int]:
    """
    Запитує у користувача, куди поставити новий символ.

    Повинна:
    - запитати координати (рядок і стовпчик),
    - перевірити, що клітинка вільна,
    - у разі помилки (зайнята/некоректна) — попросити ввести ще раз.

    :param player_name: str - Ім'я поточного гравця (наприклад, "Гравець X").
    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: tuple[int, int] - Пара (row, col) з коректними координатами для ходу.
    """
    # TODO:
    # 1. В циклі питати в користувача рядок та стовпчик (через input()).
    # 2. Перевіряти:
    #    - чи це числа;
    #    - чи знаходяться в межах сітки;
    #    - чи клітинка вільна.
    # 3. Якщо все добре — повернути (row, col).
    # 4. Якщо ні — вивести повідомлення про помилку і повторити.
    size = len(grid)
    while True:
        print(f"{player_name}, ваш хід.")
        row_input = input("Введіть номер рядка : ")
        col_input = input("Введіть номер стовпчика : ")

        if not (row_input.isdigit() and col_input.isdigit()):
            print("Помилка! Введіть цілі числа. Спробуйте ще раз.")
            continue

        row = int(row_input)
        col = int(col_input)

        if row < 0 or row >= size or col < 0 or col >= size:
            print("Помилка!")
            continue

        if grid[row][col] != " ":
            print("Помилка! Ця клітинка вже зайнята. Виберіть іншу.")
            continue

        return (row, col)


def check_winner(grid: list[list[Cell]]) -> Symbol | None:
    """
    Перевіряє, чи є переможець на поточній сітці.

    Перевіряються:
    - усі рядки,
    - усі стовпці,
    - дві діагоналі (головна і побічна).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: Optional[Symbol] - "X", якщо виграв хрестик,
                                "O", якщо виграв нулик,
                                None, якщо переможця ще немає.
    """
    # TODO:
    # 1. Перевірити кожний рядок: всі елементи однакові та не " ".
    # 2. Перевірити кожний стовпець.
    # 3. Перевірити дві діагоналі.
    # 4. Якщо знайдено три однакові символи ("X" або "O") — повернути їх.
    # 5. Якщо переможця немає — повернути None.

    size = len(grid)
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] and grid[i][0] != " ":
            return grid[i][0]

    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] and grid[0][i] != " ":
            return grid[0][i]

    if grid[0][0] != " ":
        symbol = grid[0][0]
        win = True
        for i in range(size):
            if grid[i][i] != symbol:
                win = False
                break
        if win:
            return symbol

    if grid[0][size - 1] != " ":
        symbol = grid[0][size - 1]
        win = True
        for i in range(size):
            if grid[i][size - 1 - i] != symbol:
                win = False
                break
        if win:
            return symbol

    return None


def has_empty_cells(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи є на сітці ще вільні (порожні) клітинки.

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо є хоч одна порожня клітинка,
                    False, якщо поле повністю заповнене.
    """
    # TODO: пройти по всіх клітинках і перевірити, чи є хоча б одна " ".
    pass


def is_game_over(grid: list[list[Cell]]) -> bool:
    """
    Перевіряє, чи гра завершена.

    Гра завершується, якщо:
    - є переможець, або
    - немає вільних клітинок (нічия).

    :param grid: list[list[Cell]] - Поточна сітка гри.
    :return: bool - True, якщо гра завершена, False інакше.
    """
    # TODO:
    # 1. Використати check_winner().
    # 2. Використати has_empty_cells().
    # 3. Повернути True, якщо є переможець або немає порожніх клітинок.
    pass


def switch_player(player: Symbol) -> Symbol:
    """
    Змінює поточного гравця.

    :param player: Symbol - Поточний символ гравця ("X" або "O").
    :return: Symbol - Інший символ ("O" якщо був "X", і навпаки).
    """
    # TODO: повернути "O" якщо player == "X", і "X" якщо player == "O".
    pass


def main() -> None:
    """
    Головна функція. Організовує всю роботу гри та запускає програму.

    Алгоритм:
    1. Створити порожню сітку.
    2. Встановити стартового гравця (наприклад, "X").
    3. У циклі:
       - вивести сітку;
       - запитати хід у поточного гравця;
       - додати символ до сітки;
       - перевірити, чи є переможець;
       - перевірити, чи ще є вільні клітинки;
       - при завершенні гри вивести результат (хто виграв або нічия);
       - переключити гравця.
    """
    # TODO: реалізувати основний ігровий цикл за описаним алгоритмом.
    pass


print_grid(create_grid(3))
