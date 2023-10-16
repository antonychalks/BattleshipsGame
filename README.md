#Welcome to Antony's Battleships

This is a Python Command-line battleships game.
The last update to this file was: **October 16, 2023**

[TOC]

## Introduction

Antony's Battleships is a classic battleship's game with many different options to customise how the game is played to make it easier or harder depending on whether the user would like a relaxed game or a challenge. In this game you can set the board size, how many ships each player has and you can even decide who goes first!

## Features

In this section, I am going to discribe step by step how the game works, and what validation is used at each step.

### Existing Features

- __"Type play to start"__

  - This is used as a 'start button' to begin running the game when the user is ready.
  - At this point there is a hidden option to type 'test' which allows any developers to skip any validation when setting up the game. For example, when I wanted to test what happens when a ship is hit, or a player wins the game, rather than playing the game on a 6x6 grid and trying to hit the computers ship over and over again, I can now by pass the "validate_board_size" function and set a 1x1 grid, which saves time in the testing phase.

![play/test]()

- __Board Size__

  - Here the user can select a board size between 6 and 26 or can enter 'random' to allow the computer to randomly generate a certain board size.
  - This section is validated using validate_board_input(xy), which checks the input in larger than 3 characters. This ensures the user has inputted the correct value. validate_int(x/y) and validate_board(x/y) are also used to make sure the input:
    - Is an integer.
    - Is between 5 and 27 (not including 5 and 27).
  - The user is then asked if they are happy with this board size, and if not, they are allowed to go back and try again

![Board Size.]()

- __Number of Ships__

  - The user is now asked how many ships are wanted.  
  - The user can either type a number, or select random.
  - validate_int(ship) is used to validate that the value given is an integer.
  - validate_ship_qty(ship) is used to ensure the input is less than the total amount of spaces on the board. If the input is more than 75% of the total spaces on board, a warning is given to the user to ensure they are happy with this.

![Number of Ships]()

- __Placing ships__

  - The user can now place the ships which is done by calling the select_coords() function. This functions asks the user for a coordinate. After this the function checks the coordinate is the correct way round, before returning the x and y coordinates.
  - The coordinates are checked to ensure they are valid and on the board.
  - The coordinate that was selected now gets changed from "~~" to "SS" to show there is a ship.
  - The computers ships are then placed using random integers.


![Placing Ships]()

- __Who goes first?__ 

  - The user can now select if they would like to go first, if they would like the computer to go first, or if they would like to randomise the choice,
  - The input is validated to those three options, and will loop back if incorrect.

![First turn]()

- __Launching a missile__

  - The two boards are then printed onto the screen. Game_board_blank is printed in place of the opposition, so as to not show the user where the oppositions ships are.
  - If the user is going first, they can now select where to fire a missile. This is done by typing the coordinates in.
  - The programme will then validate that the input is the correct format, before checking if there is an enemy ship there. 
  - If there is an enemy ship, the space will change to '><' to denote that a ship has been hit.
  - If there isn't a ship then the space with change to 'xx' to show that it was missed.
  - If the coordinates have already been fired upon, an error will pop up, allowing the user to go again.
  - The computer then takes their turn.
  - This continues until either player has lost all their ships, in which case the other player wins.

![Missile Fired.]()

### Features Left to Implement

- Another feature idea

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 

You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site


Congratulations on completing your Readme, you have made another big stride in the direction of being a developer! 

## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 