# ------ Global variables -------

board = {1: "-", 2: "-", 3: "-",
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}

game_still_running = True

current_player = "X"


# ------ Functions --------
def play_game():
    """
    Starts the game by displaying the board
    """

    display_board(board)

    while game_still_running:

        handle_turn(current_player)

        flip_player()


def display_board(board):
    """
    Display the board to screen
    """
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")


def handle_turn(player):
    """
    Get position from player and makes sure
    it's a valid input and spot is open
    """
    try:
        print(player + " 's turn.")
        position = int(input("Choose a position from 1 to 9: "))
    except ValueError:
        print("Input must be a number, try again")
        position = int(input("Choose a position from 1 to 9: "))

    if position < 1 or position > 9:
        print("Wrong input! Choose a number from 1 - 9")
        position = int(input("Choose a position from 1 to 9: "))

    if board[position] != "-":
        print("You can't go there. Go again")
        position = int(input("Choose a position from 1 to 9: "))

    insert_player(player, position)


def check_space(position):
    """
    Check if the space of the position is free
    and return either True or False
    """
    if(board[position] == "-"):
        return True
    else:
        return False


def insert_player(player, position):
    """
    Adds the player to the board and checks if we have
    a winner or if it's a tie
    """
    if check_space(position):
        board[position] = player
        display_board(board)
        if check_draw():
            print("It's a tie!")
            exit()
        if check_win():
            if player == "X":
                print("X wins!")
                exit()
            else:
                print("O wins!")
                exit()


def check_win():
    """
    All possible winning combinations.
    Algorithm from Java Coding Community - Programming Tutorials
    """
    if (board[1] == board[2] and board[1] == board[3] and board[1] != "-"):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != "-"):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != "-"):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != "-"):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != "-"):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != "-"):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != "-"):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != "-"):
        return True
    else:
        return False


def check_draw():
    """
    Check if game is draw
    """
    for key in board.keys():
        if board[key] == "-":
            return False

    return True


def flip_player():
    """
    Flips the current player from X to 0 and
    other way around.
    """
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


print("This is a simple game of Tic-Tac-Toe")
print("\n")
print("Positions are as follows:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

play_game()
