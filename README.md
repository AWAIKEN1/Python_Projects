# Alistair's Tic_Tac_Toe Game 

This code is an implementation of a simple command-line Tic Tac Toe game in Python.

The game starts by displaying a board with numbers from 1-9 representing the different spots. The players take turns picking a spot on the board by entering a number between 1-9. The first player to get three in a row wins the game. If all the spots are filled up and there is no winner, the game ends in a draw.

The code uses the draw_board() function from the helpers module to draw the Tic Tac Toe board. It also uses the check_turn() and check_for_win() functions to determine the winner of the game. The os module is used to clear the screen after every turn to make the game more visually appealing.

The while loop in the code keeps the game running until a winner is declared or the players quit the game. The if statements check if the player input is valid and if the chosen spot is already taken.

After the game ends, the board is displayed one last time along with the winner's name, if there is a winner.


Make sure you have python installed on your local machine. 

Clone your fork of this repository to your local machine and `cd` into it:

```sh
$ git clone "your fork's URL"

$ cd Tic_Tac_Toe
```


The first task is to set up your **virtual environment**.

Run this command in a terminal:
```bash
make create-environment
```

You should see the `venv` directory appear within the project folder.

Using `make` as described below wil mean you don't have to activate your environment.


To play the game open in Visual Studio code and cd into main directory Tic_Tac_Toe. In your terminal run the following command.

```
python src/main.py
```

Now you are ready to play! 





If you want to check the code is working you can run the tests I have provided. 


Install `pytest` by running:
```bash
make pytest
```

The `pytest` library will be used for unit tests. Additionally, there will be `flake8` checks to make sure for PEP8 compliance in the later katas, this will be checked via `make`. 

In the terminal, navigate to the root directory of the project, and run:

```
make flake
```

Then, you can use the command below to run your all tests and check for PEP8 compliance:

```
make run-checks
```




