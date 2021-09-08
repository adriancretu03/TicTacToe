board = ["-" for position in range(9)]

game_is_on = True
winner = None
current_player = "X"

x_score = 0
y_score = 0


def display_board():
    print(board[0] + "|" + board[1] + "|" + board[2])
    print(board[3] + "|" + board[4] + "|" + board[5])
    print(board[6] + "|" + board[7] + "|" + board[8])

    return

def pick_one(player):
    valid_position = False

    while not valid_position:
        position = input(f"Player {player}, choose a position from 1 to 9: ")
        if position.isdigit() and int(position) in range(1,10):
            position = int(position) - 1

            if board[position] != '-':
                print('Place taken, choose another one.')
            else:
                valid_position = True
            
        else:
            print('Read again')
            
    board[position] = player

    display_board()

    return

def check_rows():
    global winner

    if board[0] == board[1] == board[2] != '-':
        winner = board[0]
    elif board[3] == board[4] == board[5] != '-':
        winner = board[3]
    elif board[6] == board[7] == board[8] != '-':
        winner = board[6]

    return

def check_columns():
    global winner 

    if board[0] == board[3] == board[6] != '-':
        winner = board[0]
    elif board[1] == board[4] == board[7] != '-':
        winner = board[1]
    elif board[2] == board[5] == board[8] != '-':
        winner = board[2]

    return

def check_diagonals():
    global winner

    if board[0] == board[4] == board[8] != '-':
        winner = board[0]
    elif board[6] == board[4] == board[2] != '-':
        winner = board[6]
        
    return

def check_if_tie():
    global game_is_on
    
    if '-' not in board and not winner:
        game_is_on = False

    return

def check_if_game_over():
    global game_is_on

    check_rows()
    check_columns()
    check_diagonals()

    if winner:
        global x_score, y_score

        game_is_on = False
        if winner == 'X':
            x_score += 1 
        else:
            y_score += 1
    else:
        check_if_tie()

    return

def flip_player():
    global current_player

    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'

def play_game():

    display_board()

    while game_is_on:
        global current_player
        pick_one(current_player)

        check_if_game_over()

        flip_player()

    if winner:
        print(f'Player {winner} won. {x_score}:{y_score}')
    else:
        print('It\'s a tie.')

while True:
    play_game()

    while True:
        choice = input("Do you want to play again? (y/n)") 
        
        if choice == 'n':
            break
        elif choice == 'y':
            board = ["-" for position in range(9)]

            game_is_on = True
            winner = None
            current_player = "X"
            break
            
    if choice == 'n':
        print(f'Final score is {x_score}:{y_score}')
        break
