import gspread
from google.oauth2.service_account import Credentials

# Constants
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleships')

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


def print_board(board):
    print("Your Board:")
    for row in board:
        print(" ".join(row))


def main():
    xy = get_board_size()
    board(xy)

main()
