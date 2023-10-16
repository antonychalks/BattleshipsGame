import string
import random
import time

game_board_blank = []
game_board_user = []
game_board_computer = []


def validate_board_input(value):
    """
    Validates that the input is more than 3 characters
    This ensures the input is valid.
    """
    if testing is True:
        print("TEST: Skipping Validation: validate_board_input")
        return True
        # Skips validation if in testing mode.
    else:
        try:
            if len(value) > 3:
                return True
                # Checks the length of value is more than 3
                # as if it's not the input will be the incorrect format.
            else:
                # Raises an error if the validation fails.
                raise ValueError("You have not used the correct format,\
                                  You need to type the first number\
                                  followed by ' x ' followed by your\
                                  second number.")
        except ValueError as e:
            # Prints the error to the user.
            print(f"Invalid input: {e}. Please try again.\n")
            return False


def validate_int(num):
    """
    Validates that the value passed is an integer and
    isn't larger than the X axis.
    """
    # Skips validation if in testing mode.
    if testing is True:
        print("TEST: Skipping Validation: validate_int")
        return True
    else:
        try:
            # Checks if the input is a number.
            num = int(num)
            if isinstance(num, int):
                return True
            else:
                raise ValueError(f"A whole number is required,\
                                you typed: {num}")
            # Checks if the number is larger than the board.
            if num > xy[0]:
                raise ValueError(f"Only one Character is allowed.")
            else:
                return True
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")
            return False


def validate_board(num):
    """
    Validates that the value passed is between the minimum (6)\
    and the maximum (26) size allowed.
    """
    # Skips validation if in testing mode.
    if testing is True:
        print("TEST: Skipping Validation: validate_board")
        return True
    else:
        try:
            # Checks the value is between 5 and 27 as this is the
            # max and min board size.
            num = int(num)
            if 5 < num < 27:
                return True
            else:
                raise ValueError(f"A number larger than 5 and smaller than\
                                27 is required. You typed {num}")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n\n")
            return False


def validate_letter(letter):
    """
    Validates that the value passed is a letter and that the numerical value\
    of that letter doesn't exceed the board size.
    """
    # Skips validation if in testing mode.
    if testing is True:
        print("TEST: Skipping Validation: validate_letter")
        return True
    else:
        try:
            # Checks if the numerical value of the letter input
            # is less than the board size.
            if letter_to_number(letter.upper()) > xy[1]:
                raise ValueError(f"{letter} is off the board.")
            else:
                return True
            if type(letter) is str:
                return True
            else:
                raise ValueError("Your input was not a letter.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again with a letter from A\
                    to {number_to_letter(xy[1])}.\n")
            return False


def validate_ship_qty(ship):
    """
    Validates that the value passed doesn't exceed the total number of spaces\
    on the board, and warns the user if the value is larger than 75% of the\
    number of spaces on the board.
    """
    # Skips validation if in testing mode.
    if testing is True:
        print("TEST: Skipping Validation: validate_ship_qty")
        return True
    else:
        try:
            # Checks if the valuse is more than the area of the board.
            ship = int(ship)
            area = xy[0] * xy[1]
            if area <= ship:
                raise ValueError(f"The number of ships entered ({ship}) is\
                                more than the available squares ({area}).")
            # Checks if the value is more that 75% the area of the board.
            if area * 0.75 <= ship:
                print(f"WARNING: The number of ships entered ({ship}) is more\
                        than 75% of the available squares ({area}).")
                while True:
                    proceed = input("Do you wish to proceed? Y/N: ")
                    if proceed == "Y":
                        return True
                    elif proceed == "N":
                        return False
                    else:
                        print("Incorrect Value.\nIf you wish to proceed please\
                            type 'Y'.\nIf you do not please enter 'N'\n")
            else:
                return True
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again with a number lower\
                    than {area}.\n")
            return False


def is_testing():
    """
    Gives a developer the option to enter test mode.
    This bipasses some validation options.
    """
    print("Type 'play' to start:")
    test = input("")
    # If the input is play it will run the game as normal.
    if test.lower() == "play":
        return False
    # If the input is test it enters test mode.
    elif test.lower() == 'test':
        print("Entering test mode...")
        return True
    else:
        print(f"Invalid Input. '{test}' Please try again.\n")
        is_testing()


def get_board_size():
    """
    Get the size of the board through user input.
    """
    print("Welcome to Python Battleships!")

    while True:
        # Gets the size of the board through use input,
        # or allows the user to select a random size.
        xy = input(f"How tall and wide would you like the board to be?\
            (Min 6, Max 26)\nPlease enter in the following format: 'X x Y'\n\
            If you would like a random board, type 'random'.\n")
        if validate_board_input(xy):
            if xy.lower() == "random":
                # Gets two random integers between 6 and 26.
                x = random.randint(6, 26)
                y = random.randint(6, 26)
                break
            else:
                # Removes white space from the input if there is any.
                for i in xy:
                    if i == " ":
                        i == ""
                # Splits the input into two different variables.
                xy = xy.split("x")
                x = int(xy[0])
                y = int(xy[1])
                # Validates the inputs.
                if validate_int(x) and validate_board(x):
                    if validate_int(y) and validate_board(y):
                        break
                    else:
                        print("'Y' value invalid, please try again")
                else:
                    print("'X' value invalid, please try again")
            print("Invalid input, Please try again.\n")
        else:
            print("Invalid format. Input should be X x Y, with a space between\
                each character and two whole numbers for the X and Y")

    while True:
        # Checks the user is happy with the board size.
        correct = input(f"You have chosen a {x} x {y} board size! Is this\
                        correct? (Y/N): ").lower()
        if correct == 'y':
            return int(x), int(y)
        elif correct == 'n':
            print("Please re-enter the board size.")
            return get_board_size()
        else:
            print("Invalid input")


def board(board_size, is_user):
    """
    Creates the board and then prints it to the user.
    """
    x, y = board_size
    # Sets game_board to a list of lists which creates the sea
    # for the board at the given size.
    game_board = [["~~" for num in range(y)] for num in range(x)]
    # Prints the board if it's for a user or computer.
    # This stops the blank board being print.
    if is_user == "user" or is_user == "computer":
        print_board(game_board, is_user)
    return game_board


def print_board(board, is_user):
    """
    Gets the board that was saved in a list and prints it with a numbers
    column and letters row so the use has coordiantes to use.
    """
    if is_user == "user":
        print("Your Board:")
    else:
        print("Computer Board:")
    # Adds the letters a long the top and joins the lists to
    # create a better looking board.
    column_headers = list(string.ascii_uppercase)[:len(board[0])]
    header_str = "   " + "  ".join(column_headers)
    print(header_str)
    # Adds an extra space after the single digit values on the Y axis.
    # Without this the board will be off center from 10 onwards.
    for i, row in enumerate(board, 1):
        if i < 10:
            print(f"{i}  {' '.join(row)}")
        else:
            print(f"{i} {' '.join(row)}")


def letter_to_number(letter):
    """
    Changes the letter into its numerical value. I.E A=1, B=2, C=3
    """
    return string.ascii_uppercase.index(letter.upper()) + 1


def number_to_letter(number):
    """
    Changes a number into the corrosponding letter from the alphabet.
    I.E 1=A, 2=B, C=3
    """
    if 1 <= number <= 26:
        return string.ascii_uppercase[number - 1]
    else:
        raise ValueError("Number must be between 1 and 26")


def ship_qty():
    """
    Gets the user input, or uses random to determine
    the number of ships each player has.
    """
    while True:
        print("How many Ships should each player have?\n")
        ship = input("You can also type 'random' for a random amount: ")
        # Gives the option for a random output.
        if ship.lower() == "random":
            ship = random.randint(1, xy[1])
            if validate_ship_qty(ship) and validate_int(ship):
                break
        if validate_ship_qty(ship) and validate_int(ship):
            break
    return int(ship)


def select_coords():
    """
    Used to recieve an input from the user
    that will select coordinates on the board.
    """
    max_y = number_to_letter(xy[1])
    yx = input(f"Please input the X and Y co-ordinates of the square you would\
                like to select. \nFor example: D12\n\
                Please do not exceed {max_y}{xy[0]}: ")
    y_letter = yx[0]
    # Checks the input is the correct way round.
    if not y_letter.isalpha():
        print("Incorrect format. You have typed a number instead of a letter\n\
                Please ensure you enter a letter followed by a number.")
        return select_coords()
    x = int(yx[1:3])
    y = letter_to_number(y_letter)
    return x, y


def place_ships(game_board, is_user):
    """
    Uses inputs from the user and random integers to determin where the ships\
        are placed on the gameboard and updates the respective gameboard.
    """
    ships_remain = num_ships

    # This code will keep running until no ships are left to place.
    while ships_remain > 0:
        if is_user == "user":
            print("Now you need to place your ships")
            print(f"You have {ships_remain} ships remaining.")
            print("Where would you like to place your ship?")
            # Runs the select_coords function,
            # which was created to keep the code clean.
            coords = select_coords()
            x, y = coords
        else:
            print("Randomising computer ships...")
            x = random.randint(1, xy[0])
            y = random.randint(1, xy[1])

        # Checks the inputted values are within the
        # correct margins, and if they are,
        # replaces the '~~' to 'SS' to show there
        # is a ship in that place.
        if 1 <= x <= len(game_board) and y <= xy[1]:
            if game_board[x - 1][y - 1] == "~~":
                game_board[x - 1][y - 1] = "SS"
                if is_user == "user":
                    print_board(game_board, is_user)
                ships_remain -= 1
            else:
                print("Sorry, a ship is already placed at those coordinates.\
                        Please try again.")
        else:
            print("Invalid coordinates. Please enter valid coordinates\
within the board size.")

    print("All ships have been placed.")


def play_game(game_board_blank, game_board_user, game_board_computer):
    """
    This function runs the main game and is used to determin
    if the user or computer goes first.
    """
    def user_first(num_ships):
        """
        Function is called to run the game if the user goes first.
        """
        user_ships = num_ships
        comp_ships = num_ships

        # The code keeps running until either the user's
        # or computers ship count reaches 0.
        while user_ships > 0 and comp_ships > 0:
            print("Time to take your turn!")
            time.sleep(0.5)
            # Calls the take turn function for the user which returns true if
            # a ship is hit, which minuses a ship from the respective
            # counter.
            if take_turn(game_board_user, game_board_computer,
                         game_board_blank, "user") is True:
                comp_ships -= 1
            # Breaks the while loop if the computers ship count reaches 0.
            if comp_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

            print("Computers turn!")
            time.sleep(2)
            # This code executes the same as above,
            # but for the computers turn.
            if take_turn(game_board_computer, game_board_user,
                         game_board_blank, "comp") is True:
                user_ships -= 1
            if user_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

        # After the while loop is broken, this code is executed
        # depending on who won.
        if comp_ships == 0:
            print("YOU WIN! Computer loses!")
        elif user_ships == 0:
            print("YOU LOSE! Computer wins!")

    def comp_first(num_ships):
        """
        Function is called to run the game if the computer goes first.
        """
        user_ships = num_ships
        comp_ships = num_ships

        while user_ships > 0 and comp_ships > 0:
            print("Computers turn!")
            time.sleep(2)
            # Calls the take turn function for the computer which returns true
            # if a ship is hit, which minuses a ship from the respective
            # counter.
            if take_turn(game_board_computer, game_board_user,
                         game_board_blank, "comp") is True:
                user_ships -= 1
            # Breaks the while loop if the computers ship count reaches 0.
            if user_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")

            print("Time to take your turn!")
            time.sleep(0.5)
            # This code executes the same as above,
            # but for the computers turn.
            if take_turn(game_board_user, game_board_computer,
                         game_board_blank, "user") is True:
                comp_ships -= 1
            if comp_ships == 0:
                break
            print(f"Your ships remaining: {user_ships}")
            print(f"Computer ships remaining: {comp_ships}")
        # After the while loop is broken, this code is executed
        # depending on who won.
        if comp_ships == 0:
            print("YOU WIN! Computer loses!")
        elif user_ships == 0:
            print("YOU LOSE! Computer wins!")

    while True:
        # This code determins if the user would like
        # themselves or the computer to go first
        # or they can select the random option.
        # The appropriate function is called.
        print("Who goes first?")
        first_turn = input("User, Computer, Random: ")
        if first_turn.lower() == "user":
            user_first(num_ships)
            break
        elif first_turn.lower() == "computer":
            comp_first(num_ships)
            break
        elif first_turn.lower() == "random":
            random_start = random.randint(1, 2)
            if random_start == 1:
                user_first(num_ships)
                break
            else:
                comp_first(num_ships)
                break
        else:
            print("Invalid input. Please try again:")


def take_turn(game_board_turn, game_board_spectator,
              game_board_blank, is_user):
    """
    This function is used each time the user or computer takes a turn.
    """
    if is_user == "user":
        # This prints a blank board, which acts as the opponants board.
        # Printing the computer board would mean showing the user
        # where all the computer's ships are located.
        print_board(game_board_blank, "blank")
        print_board(game_board_turn, "user")
        print("Now you need to chose where to launch missile")
        coords = select_coords()
        x, y = coords
        print(number_to_letter(y)+str(x))
    else:
        # If it is not the users turn then two random integers are
        # passed as the co-ordinates.
        print("Computer taking their turn")
        x = random.randint(1, xy[0])
        y = random.randint(1, xy[1])
        print(number_to_letter(y)+str(x))

    # Checks the inputted values are within the
    # correct margins, and if they are, checks if
    # that position has already been fired at.
    if 1 <= int(x) <= len(game_board_spectator) and y <= xy[1]:
        if game_board_spectator[x - 1][y - 1] == "xx" or\
           game_board_spectator[x - 1][y - 1] == "><":
            print("Co-ordinates already selected!")
            # This allows the user to take another go.
            take_turn(game_board_turn, game_board_spectator,
                      game_board_blank, is_user)
        else:
            # Checks if there is a ship on the selected
            # coordinates. If there is it prints hit and
            # returns true so the ship count decreases by 1.
            if game_board_spectator[x - 1][y - 1] == "SS":
                game_board_spectator[x - 1][y - 1] = "><"
                if is_user == "user":
                    game_board_blank[x - 1][y - 1] = "><"
                print("HIT!")
                return True
            # If there isn't a ship then "Miss" is
            # printed and nothing happens.
            elif game_board_spectator[x - 1][y - 1] == "~~":
                game_board_spectator[x - 1][y - 1] = "xx"
                print("MISS!")
                if is_user == "user":
                    game_board_blank[x - 1][y - 1] = "xx"
    else:
        print("Invalid coordinates. Please enter valid coordinates within\
              the board size.")
        # Calling the function allows the user to take another turn.
        take_turn(game_board_turn, game_board_spectator,
                  game_board_blank, is_user)
    print("Changing player...")
    time.sleep(2)


def main():
    """
    This is the main function called to run everything in the correct order.
    """
    global xy
    global testing
    global num_ships
    global game_board_blank
    global game_board_user
    global game_board_computer

    # Checks if the user wants to test.
    testing = is_testing()
    # Gets the board size from the user and passes it to the global variable.
    xy = get_board_size()
    # Sets the three different boards used
    # and passes them to the global variable.
    game_board_blank = board(xy, "blank")
    game_board_user = board(xy, "user")
    game_board_computer = board(xy, "computer")
    # Sets the number of ships each player has for the game
    # and passes it to the global variable.
    num_ships = ship_qty()
    # Calls the function to place the user's ships.
    place_ships(game_board_user, "user")
    # Calls the function to place the computer's ships
    place_ships(game_board_computer, "computer")
    # Runs the game once all the setup functions are complete.
    play_game(game_board_blank, game_board_user, game_board_computer)


# Runs the programme
main()
