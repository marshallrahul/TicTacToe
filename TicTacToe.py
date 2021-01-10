import random
from time import sleep


# Creat an empty board
def create_board(board):
    print('    |   | ')
    print('  ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('    |   | ')
    print('-------------')
    print('    |   | ')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('    |   | ')
    print('-------------')
    print('    |   | ')
    print('  ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('    |   | ')


# Choose marker
def choose_marker():
    marker = input("Choose a marker between X or O: ").upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# Player input on the board
def player_input(board, marker):
    while True:
        position = int(input("Choose your position (1-9): "))
        if position in [1, 2, 3, 4, 5, 6, 7, 8, 9] and check_empty_places(board, position):
            board[position] = marker
            return False
        else:
            print("\nInvalid number!!! Go again.")


# Check for empty places on board
def check_empty_places(board, position):
    return board[position] == ' '

# Select random place for the computer
def random_place(board, marker):
    while True:
        position = random.choice(range(1, 10))
        if position in [1, 2, 3, 4, 5, 6, 7, 8, 9] and check_empty_places(board, position):
            board[position] = marker
            return False


# Check three of their marker in horizontal row
def row_win(board, marker):
    return ((board[1] == board[2] == board[3] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[7] == board[8] == board[9] == marker))


# Check three of their marker in vertical row
def col_win(board, marker):
    return ((board[1] == board[4] == board[7] == marker) or
    (board[2] == board[5] == board[8] == marker) or
    (board[3] == board[6] == board[9] == marker)
)

# Check three of their marker in diagonal row
def dig_win(board, marker):
    return ((board[1] == board[5] == board[9] == marker) or
    (board[3] == board[5] == board[7] == marker))


# evaluate the Winner
def evaluate(board, marker):
    return (row_win(board, marker) or col_win(board, marker) or dig_win(board, marker))


# Check weather there is a winner
def board_check(board, position):
    return board[position] != ' '


# Check weathe the game is tie
def full_board_check(board):
    for i in range(1, 10):
        if board_check(board, i):lackj
            return False
    return True


# Main fuction to start the Game now
def play_game():

    player1_marker, player2_marker = choose_marker()
    print("You : {}".format(player1_marker))
    print("Computer : {}".format(player2_marker))

    the_board = [' ']*10
    keys = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    create_board(keys)

    while True:
        print("Your turn: ")
        player_input(the_board, player1_marker)
        print("\n")
        create_board(the_board)
        if evaluate(the_board, player1_marker):
            print("Congratulation!!! You won the game.")
            break
        else:
            if full_board_check(the_board):
                print("TIE!!!")
                break

        print("\n")
        print("Computer's turn: ")
        sleep(2)
        random_place(the_board, player2_marker)
        print("\n")
        create_board(the_board)
        if evaluate(the_board, player2_marker):
            print("Congratulation!!! Computer won the game.")
            break
        else:
            if full_board_check(the_board):
                print("TIE!!!")
                break

play_game()
