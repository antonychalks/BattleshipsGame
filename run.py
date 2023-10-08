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


def get_board_size(testing):
    """
    Get the size of the board through user input.
    """
    print("Welcome to Python Battleships!")
    while True:
        x = input("How tall would you like the board to be? ")
        if validate_int(x, testing) and validate_5(x, testing):
            break

    while True:
        y = input("How wide would you like the board to be? ")
        if validate_int(y, testing) and validate_5(y, testing):
            break

    correct = input(f"You have chosen a {x} x {y} board size! Is this correct? (Y/N): ").lower()
    if correct == 'y':
        return int(x), int(y)
    else:
        print("Please re-enter the board size.")
        return get_board_size(testing)


def validate_int(num, testing):
    if is_testing:
        print("Skipping Validation: validate_int")
        return True
    else:
        try:
            if num.isnumeric():
                return True
            else:
                raise ValueError(f"A whole number is required, you typed: {num}")
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False


def validate_5(num, testing):
    if is_testing:
        print("Skipping Validation: validate_5")
        return True
    else:
        try:
            if int(num) >= 6:
                return True
            else:
                raise ValueError(f"A number larger than 5 is required. You typed {num}")
        except ValueError as e:
            print(f"Invalid data: {e}. Please try again.")
            return False


def validate_letter(letter, game_board, testing):
    if is_testing:
        print("Skipping Validation: validate_letter")
        return True
    else:
        if letter.upper() in string.ascii_uppercase[:5]:
            return True
        else:
            print("Invalid letter input. Please enter a letter from A to E.")
            return False


def board(board_size, is_user):
    x, y = board_size
    game_board = [["~~" for _ in range(y)] for _ in range(x)]
    if is_user == "user" or is_user == "computer":
        print_board(game_board, is_user)
    return game_board


def print_board(board, is_user):
    if is_user == "user":
        print("Your Board:")
    else:
        print("Computer Board:")
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


def place_ships(xy, game_board, qty, is_user):
    ships_remain = qty
    max_y = number_to_letter(xy[1])

    while ships_remain > 0:
        if is_user == "user":
            print("Now you need to place your ships")
            print(f"You have {ships_remain} ships remaining.")
            y_letter = input(f"Please input the Y axis of the ship you would like to place (A to {max_y}): ")
            x = int(input(f"Please input the X axis of the ship you would like to place (1 to {xy[0]}): "))
            y = letter_to_number(y_letter)
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

    print("Who goes first?")
    first_turn = input("User, Computer, Random: ")

    if first_turn.lower() == "user":
        user_first(num_ships)
    elif first_turn.lower() == "computer":
        comp_first(num_ships)
    elif first_turn.lower(num_ships) == "random":
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
        y_letter = input(f"Please input the Y axis of the position you would like to target (A to {max_y}): ")
        x = int(input(f"Please input the X axis of the position you would like to target (1 to {xy[0]}): "))
        y = letter_to_number(y_letter)
        print(number_to_letter(y)+str(x))
    else:
        print("Computer taking their turn")
        x = random.randint(1, xy[0])
        y = random.randint(1, xy[1])
        print(number_to_letter(y)+str(x))
            
    if 1 <= x <= len(game_board_spectator) and y <= xy[1]:
        if game_board_spectator[x - 1][y - 1] == "xx" or game_board_spectator[x - 1][y - 1] == "><":
            print("Co-ordinates already selected!")
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
    print("Changing player...")
    time.sleep(2)


def main():
    testing = is_testing()
    xy = get_board_size(testing)
    game_board_blank = board(xy, "blank")
    game_board_user = board(xy, "user")
    game_board_computer = board(xy, "computer")
    num_ships = ship_qty()
    place_ships(xy, game_board_user, num_ships, "user") 
    place_ships(xy, game_board_computer, num_ships, "computer") 
    play_game(game_board_blank, game_board_user, game_board_computer, num_ships, xy)


main()