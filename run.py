board = ["X", "-", "-", 
         "-", "-", "-",
         "-", "-", "-"]


def display_board():
    """
    Display the board to screen
    """
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def check_space(position):
    if(board[position] == "-"):
        return True
    else:
        return False


print(check_space(0))


def handle_turn():
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
    display_board()

    handle_turn()


start_game()       
