from helpers import draw_board, check_turn, check_for_win
import os


spots = {1: '1', 2: '2', 3: '3', 4: '4',
         5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


draw_board(spots)

playing = True
complete = False
turn = 0
previous_turn = -1

while playing:
    # reset the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)
    # if invalid turn has occured, let the player know
    if previous_turn == turn:
        print("Invalid spot picked, pick another please")
    previous_turn = turn
    print("Player " + str((turn % 2) + 1) +
          "'s turn: Pick your spot or press q to quit.")

    # Getting Input from the player
    choice = input()
    if choice == 'q':
        playing = False
    # check if player input is a number from 1-9
    elif str.isdigit(choice) and int(choice) in spots:
        # check if the spot has already been taken
        if not spots[int(choice)] in {'X', 'O'}:
            turn += 1
            spots[int(choice)] = check_turn(turn)

    # check if the game has finished and if there is a winner
    if check_for_win(spots):
        playing, complete = False, True
    if turn > 8:
        playing = False

# Draw board one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# if there was a winner tells us who has won

if complete:
    if check_turn(turn) == 'X':
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")

else:
    # Tie Game
    print('No Winner, you are both great')

print("Thanks for playing")
