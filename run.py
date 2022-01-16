board = {1: "-", 2: "-", 3: "-", 
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}

game_still_running = True

current_player = "X"

def play_game():

    while game_still_running:

        handle_turn(current_player)

        check_if_game_over()



def display_board(board):
    """
    Display the board to screen
    """
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("\n")


def check_space(position):
    """
    Check if the space of the position is free
    and return either True or False
    """
    if(board[position] == "-"):
        return True
    else:
        return False


def insert_game_piece(game_piece, position):
    """
    If the space is free add the game piece
    and check if any player has won.
    If not return another input.
    """
    if check_space(position):
        board[position] = game_piece
        display_board(board)

        if check_draw():
            print("Draw!")
            exit()

        if check_win():
            if game_piece == "X":
                print("Player 1 wins!")
                exit()
            else:
                print("Player 2 wins!")
                exit()
        
        return
    
    else:
        print("Can't insert there...")
        position = int(input("Enter new position (1-9): "))
        insert_game_piece(game_piece, position)
        return


def check_win():
    # All possible winning combinations
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


def player_move():
    """
    Input for the player move
    """
    position = int(input("Enter a position: "))
    insert_game_piece(player, position)
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"

    elif current_player == "O":
        current_player = "X"


print("You start! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

play_game()