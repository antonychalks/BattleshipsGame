import string
import random
import time

game_board_blank = []
game_board_user = []
game_board_computer = []


def is_testing():
    print("Type 'play' to start:")
    test = input("")
    if test.lower() == "play":
        return False
    elif test.lower() == 'test':
        print("Entering test mode...")
        return True
    else:
        print(f"Invalid Input. '{test}' Please try again.")
        is_testing()


def get_board_size():
    """
    Get the size of the board through user input.
    """
    print("Welcome to Python Battleships!")
    
    while True:
        xy = input(f"How tall and wide would you like the board to be? (Min 6, Max 26)\nPlease enter in the following format: 'X x Y'\nIf you would like a random board, type 'random'.\n")
        if validate_board_size(xy):
            if xy.lower() == "random":
                x = random.randint(6, 26)
                y = random.randint(6, 26)
                break
            else:
                xy = xy.split(" x ")
                x = int(xy[0])
                y = int(xy[1])
                if validate_int(x) and validate_board(x):
                    if validate_int(y) and validate_board(y):
                        break
                    else:
                        print("y value invalid, please try again")
                else:
                    print("x value invalid, please try again")
            print("Invalid input, please try again.")
        else:
            print("Invalid format. Input should be X x Y, with a space between each character and two whole numbers for the X and Y")

    while True:
        correct = input(f"You have chosen a {x} x {y} board size! Is this correct? (Y/N): ").lower()
        if correct == 'y':
            return int(x), int(y)
            break
        elif correct == 'n':
            print("Please re-enter the board size.")
            return get_board_size()
            break
        else:
            print("Invalid input")


def validate_board_size(value):

    try:
        if len(value) > 4:
            return True
        else:
            raise ValueError("You have not used the correct format, You need to type the first number followed by ' x ' followed by your second number.")
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.")
        return False


def validate_int(num):
    if testing == True:
        print("TEST: Skipping Validation: validate_int")
        return True
    else:
        try:
            num = int(num)
            if isinstance(num, int):
                return True
            else:
                raise ValueError(f"A whole number is required, you typed: {num}")
            if num > xy[0]:
                raise ValueError(f"Only one Character is allowed.")
            else:
                return True
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False


def validate_board(num):
    if testing == True:
        print("TEST: Skipping Validation: validate_board")
        return True
    else:
        try:
            num = int(num)
            if 5 < num < 27:
                return True
            else:
                raise ValueError(f"A number larger than 5 and smaller than 27 is required. You typed {num}")
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False


def validate_letter(letter, game_board):
    if testing == True:
        print("TEST: Skipping Validation: validate_letter")
        return True
    else:
        try:
            if letter_to_number(letter.upper()) > xy[1]:
                raise ValueError(f"Invalid letter input.")
                return False
            else:
                return True
            if type(letter) is str:
                return True
            else:
                raise ValueError("Your input was not a letter.")
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again with a letter from A to {number_to_letter(xy[1])}.")
            return False


def validate_ship_qty(ship):
    if testing:
        print("TEST: Skipping Validation: validate_ship_qty")
        return True
    else:
        try:
            ship = int(ship)
            area = xy[0] * xy[1]
            if area <= ship:
                raise ValueError(f"The number of ships entered ({ship}) is more than the available squares ({area}).")
            
            if area * 0.75 <= ship:
                print(f"WARNING: The number of ships entered ({ship}) is more than 75% of the available squares ({area}).")
                while True:
                    proceed = input("Do you wish to proceed? Y/N: ")
                    if proceed == "Y":
                        return True
                    elif proceed == "N":
                        return False
            else:
                return True  # Move this line outside of the else block
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again with a number lower than {area}.")
            return False

                    
def board(board_size, is_user):
    x, y = board_size
    game_board = [["~~" for num in range(y)] for num in range(x)]
    if is_user == "user" or is_user == "computer":
        print_board(game_board, is_user)
    return game_board


def print_board(board, is_user):
    if is_user == "user":
        print("Your Board:")
    else:
        print("Computer Board:")
    column_headers = list(string.ascii_uppercase)[:len(board[0])]
    header_str = "   " + "  ".join(column_headers)
    print(header_str)
    for i, row in enumerate(board, 1):
        if i < 10:
            print(f"{i}  {' '.join(row)}")
        else:
            print(f"{i} {' '.join(row)}")


def letter_to_number(letter):
    return string.ascii_uppercase.index(letter.upper()) + 1


def number_to_letter(number):
    if 1 <= number <= 26:
        return string.ascii_uppercase[number - 1]
    else:
        raise ValueError("Number must be between 1 and 26")


def ship_qty():
    while True:
        print("How many Ships should each player have?\n")
        ship = input("You can also type random for a random amount: ")
        if ship.lower() == "random":
            ship = random.randint(1, xy[1])
            if validate_ship_qty(ship) and validate_int(ship):
                break
        if validate_ship_qty(ship) and validate_int(ship):
            break
    return int(ship)


def select_coords():
    max_y = number_to_letter(xy[1])
    yx = input(f"Please input the X and Y co-ordinates of the square you would like to select. \nFor example: D12\nPlease do not exceed {max_y}{xy[0]}: ")
    y_letter = yx[0]
    x = int(yx[1:3])
    y = letter_to_number(y_letter)
    return x, y


def place_ships(xy, game_board, qty, is_user):
    ships_remain = qty

    while ships_remain > 0:
        if is_user == "user":
            print("Now you need to place your ships")
            print(f"You have {ships_remain} ships remaining.")
            print("Where would you like to place your ship?")
            coords = select_coords()
            x, y = coords
        else:
            print("Randomising computer ships...")
            x = random.randint(1, xy[0])
            y = random.randint(1, xy[1])

        if 1 <= x <= len(game_board) and y <= xy[1]:
            if game_board[x - 1][y - 1] == "~~":
                game_board[x - 1][y - 1] = "SS"
                if is_user == "user":
                    print_board(game_board, is_user)
                ships_remain -= 1
            else:
                print("Sorry, a ship is already placed at those coordinates. Try again.")
        else:
            print("Invalid coordinates. Please enter valid coordinates within the board size.")

    print("All ships have been placed.")


def play_game(game_board_blank, game_board_user, game_board_computer, num_ships, xy):       
    def user_first(num_ships):
        user_ships = num_ships
        comp_ships = num_ships

        while user_ships > 0 and comp_ships > 0:
            print("Time to take your turn!")
            time.sleep(2)
            if take_turn(game_board_user, game_board_computer, game_board_blank, "user", xy) == True:
                comp_ships -= 1
            if comp_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

            print("Computers turn!")
            time.sleep(2)
            if take_turn(game_board_computer, game_board_user, game_board_blank, "comp", xy) == True:
                user_ships -= 1
            if user_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

        if comp_ships == 0:
            print("YOU WIN! Computer loses!")
        elif user_ships == 0:
            print("YOU LOSE! Computer wins!")


    def comp_first(num_ships):
        user_ships = num_ships
        comp_ships = num_ships

        while user_ships > 0 and comp_ships > 0:
            print("Computers turn!")
            time.sleep(2)
            if take_turn(game_board_computer, game_board_user, game_board_blank, "comp", xy) == True:
                user_ships -= 1
            if user_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

            print("Time to take your turn!")
            time.sleep(2)
            if take_turn(game_board_user, game_board_computer, game_board_blank, "user", xy) == True:
                comp_ships -= 1
            if comp_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")
        
        if comp_ships == 0:
            print("YOU WIN! Computer loses!")
        elif user_ships == 0:
            print("YOU LOSE! Computer wins!")

    while True:
        print("Who goes first?")
        first_turn = input("User, Computer, Random: ")
        if first_turn.lower() == "user":
            user_first(num_ships)
        elif first_turn.lower() == "computer":
            comp_first(num_ships)
        elif first_turn.lower() == "random":
            random_start = random.randint(1, 2)
            if random_start == 1:
                user_first(num_ships)
            else:
                comp_first(num_ships)  
        else:
            print("Invalid input. Please try again:")



def take_turn(game_board_turn, game_board_spectator, game_board_blank, is_user, xy):
    max_y = number_to_letter(xy[1])

    if is_user == "user":
        print_board(game_board_blank, "blank")
        print_board(game_board_turn, "user")
        print("Now you need to chose where to launch missile")
        coords = select_coords()
        x, y = coords
        print(number_to_letter(y)+str(x))
    else:
        print("Computer taking their turn")
        x = random.randint(1, xy[0])
        y = random.randint(1, xy[1])
        print(number_to_letter(y)+str(x))
    
    if 1 <= int(x) <= len(game_board_spectator) and y <= xy[1]:
        if game_board_spectator[x - 1][y - 1] == "xx" or game_board_spectator[x - 1][y - 1] == "><":
            print("Co-ordinates already selected!")
            take_turn(game_board_turn, game_board_spectator, game_board_blank, is_user, xy)
        else:
            if game_board_spectator[x - 1][y - 1] == "SS":
                game_board_spectator[x - 1][y - 1] = "><"
                if is_user == "user":
                    game_board_blank[x - 1][y - 1] = "><"
                print("HIT!")
                return True
            elif game_board_spectator[x - 1][y - 1] == "~~":
                game_board_spectator[x - 1][y - 1] = "xx"
                print("MISS!")
                if is_user == "user":
                    game_board_blank[x - 1][y - 1] = "xx"
    else:
        print("Invalid coordinates. Please enter valid coordinates within the board size.")
        take_turn(game_board_turn, game_board_spectator, game_board_blank, is_user, xy)
    print("Changing player...")
    time.sleep(2)


def main():
    global xy
    global testing
    global num_ships
    testing = is_testing()
    xy = get_board_size()
    game_board_blank = board(xy, "blank")
    game_board_user = board(xy, "user")
    game_board_computer = board(xy, "computer")
    num_ships = ship_qty()
    place_ships(xy, game_board_user, num_ships, "user") 
    place_ships(xy, game_board_computer, num_ships, "computer") 
    play_game(game_board_blank, game_board_user, game_board_computer, num_ships, xy)


main()