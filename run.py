board = ["-", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"]


def display_board(board):
    """
    Display the board to screen
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_space(position):
    """
    Check if the space of the position is free
    and return either True or False
    """
    if(board[position] == "-"):
        return True
    else:
        return False


def check_win(game_piece, position):
    # All possible winning combinations
    soln = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], 
            [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
 
    # Loop to check if any winning combination is satisfied
    for x in soln:
        if all(y in position[game_piece] for y in x):
 
            # Return True if any winning combination satisfies
            return True
    # Return False if no combination is satisfied       
    return False       
 

# Function to check if the game is drawn
def check_draw(position):
    if len(position['X']) + len(position['O']) == 9:
        return True
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

        if check_win(game_piece, position):
            if game_piece == "X":
                print("Player 1 wins!")
                exit()
            else:
                print("Player 2 wins!")
                exit()
    
    else:
        print("Can't insert there...")
        position = int(input("Enter new position (1-9): "))
        insert_game_piece(game_piece, position)
        
    return


"""
def check_rows():
     return


def check_cols():
    return


def check_diagonal():
    return


def check_tie():
    return


def flip_player():    
    return
"""    


insert_game_piece("x", 1)
insert_game_piece("x", 1)   
