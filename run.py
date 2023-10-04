import gspread
import pprint
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleships')


def get_size():
    """
    Used to get the size of the board through user input
    """
    print("Welcome to python battleships!")
    while True:
        x = input("How wide would you like the board to be? ")
        y = input("How tall would you like the board to be? ")
        if validate_input(x):
            if validate_input(y):
                correct = input(f"You have chosen a {x} x {y} board size! Is this correct? Y/N:")
                if correct.lower() == 'y':
                    break

    xy = [x, y]
    return xy


def validate_input(num):
    try:
        if num.isnumeric():
            return True
        else:
            raise ValueError(f"A whole number is required, you typed: {num}")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")
        return False




def main():
    xy = get_size()

main()
