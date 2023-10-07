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


def validate_letter(letter, game_board):
    if letter.upper() in string.ascii_uppercase[:5]:
        return True
    else:
        print("Invalid letter input. Please enter a letter from A to E.")
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


def letter_to_number(letter):
    return string.ascii_uppercase.index(letter.upper()) + 1


def number_to_letter(number):
    if 1 <= number <= 26:
        return string.ascii_uppercase[number - 1]
    else:
        raise ValueError("Number must be between 1 and 26")


def ship_qty():
    ship = input("How many Ships should each player have?\n")
    return int(ship)


def place_ships(xy, game_board, qty):
    print("Now you need to place your ships")
    ships_remain = qty
    max_y = number_to_letter(xy[1])

    while ships_remain > 0:
        print(f"You have {ships_remain} ships remaining.")
        y_letter = input(f"Please input the Y axis of the ship you would like to place (A to {max_y}): ")
        x = int(input(f"Please input the X axis of the ship you would like to place (1 to {xy[0]}): "))
        
        y = letter_to_number(y_letter)
        if 1 <= x <= len(game_board) and y <= xy[1]:
            if game_board[x - 1][y - 1] == "~~":
                game_board[x - 1][y - 1] = "SS"
                print_board(game_board)
                ships_remain -= 1
            else:
                print("Sorry, a ship is already placed at those coordinates. Try again.")
        else:
            print("Invalid coordinates. Please enter valid coordinates within the board size.")

    print("All ships have been placed.")


def main():
    xy = get_board_size()
    game_board = board(xy)
    num_ships = ship_qty()  # Call the ship_qty function to get the number of ships
    place_ships(xy, game_board, num_ships)  # Pass the number of ships to place_ships


main()

