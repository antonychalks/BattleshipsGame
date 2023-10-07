import string

def get_board_size():
    """
    Get the size of the board through user input.
    """
    print("Welcome to Python Battleships!")
    while True:
        x = input("How tall would you like the board to be? ")
        if validate_int(x) and validate_5(x):
            break

    while True:
        y = input("How wide would you like the board to be? ")
        if validate_int(y) and validate_5(y):
            break

    correct = input(f"You have chosen a {x} x {y} board size! Is this correct? (Y/N): ").lower()
    if correct == 'y':
        return int(x), int(y)
    else:
        print("Please re-enter the board size.")
        return get_board_size()


def validate_int(num):
    try:
        if num.isnumeric():
            return True
        else:
            raise ValueError(f"A whole number is required, you typed: {num}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False


def validate_5(num):
    try:
        if int(num) >= 6:
            return True
        else:
            raise ValueError(f"A number larger than 5 is required. You typed {num}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False


def board(board_size):
    x, y = board_size
    game_board = [["~~" for _ in range(y)] for _ in range(x)]
    print_board(game_board)
    return game_board


def print_board(board):
    print("Your Board:")
    column_headers = list(string.ascii_uppercase)[:len(board[0])]
    header_str = "  " + "  ".join(column_headers)
    print(header_str)
    for i, row in enumerate(board, 1):
        print(f"{i} {' '.join(row)}")


def place_ships():
    print("Now you need to place your ships")
    


def main():
    xy = get_board_size()
    game_board = board(xy)
    place_ships()

main()
