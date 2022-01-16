board = {1: "-", 2: "-", 3: "-", 
         4: "-", 5: "-", 6: "-",
         7: "-", 8: "-", 9: "-"}


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


def check_mark(mark):
    # All possible winning combinations
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
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
    position = int(input("Enter a position for 'player 1': "))
    insert_game_piece(player1, position)
    return


def bot_move():
    best_score = -1000
    best_move = 0

    for key board.key():
        if board[key] == "-":
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = "-"
            if score > best_score:
                best_score = score
                best_move = key
    
    insert_game_piece(bot, best_move)
    return


def minimax(board, depth, isMaximizing):
    if check_mark(bot):
        return 1

    elif check_mark(player):
        return -1


while not check_win():
    player_move()
    bot_move()()