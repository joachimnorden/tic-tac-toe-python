board = ["X", "-", "-", 
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


def insert_game_piece(game_piece,position):
    
    if check_space(position):
        board[position] = game_piece
        display_board(board)
    
    else:
        print("Can't insert there...")
        position = input("Enter new position: ")
        insert_game_piece(game_piece, position)
        return


def check_win():
    return


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


def start_game():
    """
    Play a game of Tic Tac Toe
    """
    display_board(board)


start_game()       
