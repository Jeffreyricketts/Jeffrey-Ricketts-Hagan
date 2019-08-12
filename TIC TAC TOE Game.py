## Tic Tac Toe Game

# What we need:
    # board
    # display
    # play game
    # handle turn
    # check win
        # check rows
        # check columns
        # check diagonals
    # check tie
    # flip player


##  ---- Global Variables ----

 # Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

 # If game is still going
game_still_going = True

 # Who won? Or tie?
winner = None

 # Who's turn is it
current_player = "X"

# Displays game board
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "   1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "   4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "   7 | 8 | 9")
    print("\n")

# Plays game of tic-tac-toe
def play_game():

    # Display initial board
    display_board()
    
    # While game is still going
    while game_still_going:

       # Handle a single turn of a player
       handle_turn(current_player)

       # CHech if game has ended
       check_if_game_over()

       # Flip to the other player
       flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie LOSERS.")


# Handle a single turn of a player
def handle_turn(player):

    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there, try again.")

    board[position] = player
    
    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():

    # Set up global variables
    global winner
    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
        # There was a winner
    elif column_winner:
        winner = column_winner
        # There was a winner
    elif diagonal_winner:
        winner = diagonal_winner
        # There was a winner
    else:
        winner = None
    

def check_rows():
    # Set up gloabl variable
    global game_still_going
    # Check if any row has the same value and are not empty 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # If any row has a match, flag game as a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return winner at X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None

def check_columns():
    global game_still_going
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column has a match, flag game as a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    # Return winner at X or O
    2
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    else:
        return None

def check_diagonals():
    global game_still_going
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    
    else:
        return None


def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
        return True
    else:
        return False

def flip_player():
    # Global variable we need
    global current_player
    # If current player is X, it changes to O and vice-versa
    if current_player == "X": # == double checks if current_player is equal to X
        current_player = "O"  # = single makes current_player = O
    elif current_player == "O":
        current_player = "X"
    return

play_game()


#display_board()  # calls the function
