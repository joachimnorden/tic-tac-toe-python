def display_board(board):
    """
    Display the board to screen
    """
    print(board[1] + " | " + board[2] + " | " + board[3])
    print(board[4] + " | " + board[5] + " | " + board[6])
    print(board[7] + " | " + board[8] + " | " + board[9])


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

         if position < 1 or position > 9:
            print("Wrong input! Try again")
        
        return
    
    else:
        print("Can't insert there. Please try again")
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


def make_move():
    position = int(input("Enter a position for", cur_player,": "))
    insert_game_piece(cur_player, position)
    return


board = {1: "-", 2: "-", 3: "-", 
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}


player1 = "0"
player2 = "X"

cur_player = player1


# player1_name = input("Enter player 1 name: ")
# player2_name = input("Enter player 2 name: ")
def play_game(cur_player):
    
    player_pos = {"X": [], "O": []}

    while True:
        display_board(board)
        try:
            print("Player ", cur_player, "turn. Enter a position: ", end="")
            position = int(input())
        except ValueError:
            print("Wrong input! Try again")
            continue

        if position < 1 or position > 9:
            print("Wrong input! Try again")
            continue

        if board[position] != "-":
            print("Place already filled. Try again")
            continue

        board[position] = game_piece

        player_pos[game_piece].append(position)




while not check_win():
    make_move_0()
    make_move_X()