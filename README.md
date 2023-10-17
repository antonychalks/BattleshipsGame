# Welcome to Antony's Battleships

This is a Python Command-line battleships game.
The last update to this file was: **October 16, 2023**

## Introduction

Antony's Battleships is a classic battleship's game with many different options to customise how the game is played to make it easier or harder depending on whether the user would like a relaxed game or a challenge. In this game you can set the board size, how many ships each player has and you can even decide who goes first!

## Features

In this section, I am going to discribe step by step how the game works, and what validation is used at each step.

### Existing Features

- __"Type play to start"__

  - This is used as a 'start button' to begin running the game when the user is ready.
  - At this point there is a hidden option to type 'test' which allows any developers to skip any validation when setting up the game. For example, when I wanted to test what happens when a ship is hit, or a player wins the game, rather than playing the game on a 6x6 grid and trying to hit the computers ship over and over again, I can now by pass the "validate_board_size" function and set a 1x1 grid, which saves time in the testing phase.

![play](https://i.ibb.co/LPyfFJm/1-Play.jpg)
![test](https://i.ibb.co/DRxLtLY/1-test.jpg)

- __Board Size__

  - Here the user can select a board size between 6 and 26 or can enter 'random' to allow the computer to randomly generate a certain board size.
  - This section is validated using validate_board_input(xy), which checks the input in larger than 3 characters. This ensures the user has inputted the correct value. validate_int(x/y) and validate_board(x/y) are also used to make sure the input:
    - Is an integer.
    - Is between 5 and 27 (not including 5 and 27).
  - The user is then asked if they are happy with this board size, and if not, they are allowed to go back and try again

![Board Size.](https://i.ibb.co/CwYjkHr/2-board-size.png)

- __Number of Ships__

  - The user is now asked how many ships are wanted.  
  - The user can either type a number, or select random.
  - validate_int(ship) is used to validate that the value given is an integer.
  - validate_ship_qty(ship) is used to ensure the input is less than the total amount of spaces on the board. If the input is more than 75% of the total spaces on board, a warning is given to the user to ensure they are happy with this.

![Number of Ships](https://i.ibb.co/f8swqcQ/3-num-ships.png)

- __Placing ships__

  - The user can now place the ships which is done by calling the select_coords() function. This functions asks the user for a coordinate. After this the function checks the coordinate is the correct way round, before returning the x and y coordinates.
  - The coordinates are checked to ensure they are valid and on the board.
  - The coordinate that was selected now gets changed from "~~" to "SS" to show there is a ship.
  - The computers ships are then placed using random integers.


![Placing Ships](https://i.ibb.co/zncPyhL/4-ship-placement.png)
![Placing Computer Ships](https://i.ibb.co/dc1QQD8/4-ship-placement-comp.png)

- __Who goes first?__ 

  - The user can now select if they would like to go first, if they would like the computer to go first, or if they would like to randomise the choice,
  - The input is validated to those three options, and will loop back if incorrect.

![First turn](https://i.ibb.co/7V0Mx0V/5-first-turn.png)

- __Launching a missile__

  - The two boards are then printed onto the screen. Game_board_blank is printed in place of the opposition, so as to not show the user where the oppositions ships are.
  - If the user is going first, they can now select where to fire a missile. This is done by typing the coordinates in.
  - The programme will then validate that the input is the correct format, before checking if there is an enemy ship there. 
  - If there is an enemy ship, the space will change to '><' to denote that a ship has been hit.
  - If there isn't a ship then the space with change to 'xx' to show that it was missed.
  - If the coordinates have already been fired upon, an error will pop up, allowing the user to go again.
  - The computer then takes their turn.
  - This continues until either player has lost all their ships, in which case the other player wins.

![Missile Fired.](https://i.ibb.co/Wcnm1zY/6-fire-missile.png)
![Game Won.](https://i.ibb.co/PGyGGKM/6-game-won.png)

### Features Left to Implement

In the future I would like to implement the following features:
    - A range for the randomly generated board size so the user can have some guidance, but doesn't have to chose.
    - An automatic tester which tests all the validation at each stage by automatically inputting certain values at each point.
    - Different difficulty levels to apply to the computer.

## Testing 

To test this programme I used different methods:
    ### Manual testing
    - I first tested the 'testing mode' worked, by applying it and ensuring I could type values not normally allowed as I worked through the programme, without throwing any errors.
    - After this I played the game as normal, firstly I tried to create a game board that was too large and too small to be allowed through the validator. I also input letters and symbols to ensure the validators would catch that the value was not an integer.
    - I then asked for 0 ships, which wasn't allowed, before asking for too many and then for more than 75% of the area to ensure the programme raised a warning.
    - Then when placing ships I entered the number first then the letter to ensure the validation caught this. I then tried entering a coordinate outside of the grid. All of this was caught correctly.
    - I then tried to play the game multiple times, entering incorrect coordinates, coordinates that were off the board, and coordinates I had already selected. I then entered an input that wasn't a coordinate, and all of this was caught.

    Throughout the whole process I wanted to ensure the user was allowed to re-enter their choice, meaning the user didn't have to run the entire programme again.

    ### Peer testing
    - I then sent the deployed programme to some friends and and family to try, as they might make mistakes I hadn't thought of. It was also possible that my instructions weren't clear enough, so I wanted to make sure they could play the game without my help.
    - This helped as a few bugs were found which I have noted in bug.txt


### Validator Testing 

- I used PEP8 on my code as well as the problems tab built into the IDE and all of the coding problems that were found have been fixed. This mostly included lines being too long.

### Unfixed Bugs

All bugs that I found were noted into [bugs.txt](bugs.txt) as I went, along with the cause and solution I found worked.

## Deployment

Deployment

To deploy this website through github heroku I completed the following steps:
1. First, log into hiroku and click create new app.
2. I then named the app and set the region to Europe, before clicking create app.
3. Then, I opened the apps dashboard.
4. I then clicked the settings tab at the top of the screen.
5. At this point I would upload the creds.JSON file if it was required.
6. I then add the two buildpacks, Heroku.Python and Heroku.NodeJS by clicking add buildpack, then selecting each pack respectively.
7. After that, I clicked on the 'deploy' tab at the top of the screen.
8. Under deployment method, I selected GITHUB and ensured the account was connected.
9. I then searched for the correct repository, then clicked the connect button,
10. Finally I enabled automatic deploys to deploy the app. This also ensures everytime I use 'git push', the heroku app is updated.


The live link can be found here - https://battleships-antony-ee8c8004c260.herokuapp.com/


## Credits 

During this project I often refered back into the Code Institute course material, as well as searching stack overflow for solutions to any problems. I did not use anyone else's code or any code from other repository's for this project.

