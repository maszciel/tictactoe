# display current board function

def display_board(brd):
    print(''.join(brd[0]))
    print(''.join(brd[1]))
    print(''.join(brd[2]))


# setting players' names

def set_name():
    player1 = input('Player 1: Choose your name: ')

    player2 = input('Player 2: Choose your name: ')

    return player1, player2


# assigning x or o to player1 and the opposite to player2. If player1_x() returns True, player1 plays as x.

def player1_x():
    sign_choice = 'wrong'

    while sign_choice not in ['x', 'o']:

        sign_choice = input(f'{names[0]}, do you want to play with x, or o? ')
        if sign_choice not in ['x', 'o']:
            print("Sorry, invalid input. Please type 'x' or 'o'.")

    if sign_choice == 'x':
        return True
    elif sign_choice == 'o':
        return False


def game_on():
    on = 'wrong'

    while on not in ['y', 'n']:

        on = input("Do you want to start? Type 'y' or 'n' ")
        if on not in ['y', 'n']:
            print("Sorry, invalid input. Please type 'y' or 'n'.")

    if on == 'y':
        return True
    elif on == 'n':
        return False


# function for x moves

def x_move(field):
    if field == '1':
        board[2][0] = ' x |'
    elif field == '2':
        board[2][1] = ' x |'
    elif field == '3':
        board[2][2] = ' x '
    elif field == '4':
        board[1][0] = '_x_|'
    elif field == '5':
        board[1][1] = '_x_|'
    elif field == '6':
        board[1][2] = '_x_'
    elif field == '7':
        board[0][0] = '_x_|'
    elif field == '8':
        board[0][1] = '_x_|'
    elif field == '9':
        board[0][2] = '_x_'

    return board


# function for o moves

def o_move(field):
    if field == '1':
        board[2][0] = ' o |'
    elif field == '2':
        board[2][1] = ' o |'
    elif field == '3':
        board[2][2] = ' o '
    elif field == '4':
        board[1][0] = '_o_|'
    elif field == '5':
        board[1][1] = '_o_|'
    elif field == '6':
        board[1][2] = '_o_'
    elif field == '7':
        board[0][0] = '_o_|'
    elif field == '8':
        board[0][1] = '_o_|'
    elif field == '9':
        board[0][2] = '_o_'

    return board


# game over x wins

def x_win(brd):
    if 'x' in brd[2][0] and 'x' in brd[2][1] and 'x' in brd[2][2]:
        return True
    elif 'x' in brd[1][0] and 'x' in brd[1][1] and 'x' in brd[1][2]:
        return True
    elif 'x' in brd[0][0] and 'x' in brd[0][1] and 'x' in brd[0][2]:
        return True

    elif 'x' in brd[0][2] and 'x' in brd[1][2] and 'x' in brd[2][2]:
        return True
    elif 'x' in brd[0][1] and 'x' in brd[1][1] and 'x' in brd[2][1]:
        return True
    elif 'x' in brd[0][0] and 'x' in brd[1][0] and 'x' in brd[2][0]:
        return True

    elif 'x' in brd[2][0] and 'x' in brd[1][1] and 'x' in brd[0][2]:
        return True
    elif 'x' in brd[2][2] and 'x' in brd[1][1] and 'x' in brd[0][0]:
        return True
    else:
        return False


# game over o wins

def o_win(brd):
    if 'o' in brd[2][0] and 'o' in brd[2][1] and 'o' in brd[2][2]:
        return True
    elif 'o' in brd[1][0] and 'o' in brd[1][1] and 'o' in brd[1][2]:
        return True
    elif 'o' in brd[0][0] and 'o' in brd[0][1] and 'o' in brd[0][2]:
        return True

    elif 'o' in brd[0][2] and 'o' in brd[1][2] and 'o' in brd[2][2]:
        return True
    elif 'o' in brd[0][1] and 'o' in brd[1][1] and 'o' in brd[2][1]:
        return True
    elif 'o' in brd[0][0] and 'o' in brd[1][0] and 'o' in brd[2][0]:
        return True

    elif 'o' in brd[2][0] and 'o' in brd[1][1] and 'o' in brd[0][2]:
        return True
    elif 'o' in brd[2][2] and 'o' in brd[1][1] and 'o' in brd[0][0]:
        return True
    else:
        return False


def player1_move(brd, name, used):
    player_1_inp = 'wrong'
    tonine = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    while player_1_inp not in tonine.difference(set(used)):

        player_1_inp = input(f'{name[0]}, choose a field number: ')
        if player_1_inp not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, invalid input. Please choose a field from 1 to 9. ")
        elif player_1_inp in used:
            print("This field is taken.")

    if player1x:
        brd = x_move(player_1_inp)
    elif not player1x:
        brd = o_move(player_1_inp)

    return brd, player_1_inp, list(used)


def player2_move(brd, name, used):
    player_2_inp = 'wrong'
    to_nine = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}

    while player_2_inp not in to_nine.difference(set(used)):

        player_2_inp = input(f'{name[1]}, choose a field number: ')
        if player_2_inp not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print("Sorry, invalid input. Please choose a field from 1 to 9. ")
        elif player_2_inp in used:
            print("This field is taken.")

    if player1x:
        brd = o_move(player_2_inp)
    elif not player1x:
        brd = x_move(player_2_inp)

    return brd, player_2_inp, list(used)


def game_over(brd):

    return [x_win(brd), o_win(brd)]


print('Welcome!\nFields:\n_7_|_8_|_9_\n_4_|_5_|_6_\n 1 | 2 | 2 ')
board = [['___|', '___|', '___'], ['___|', '___|', '___'], ['   |', '   |', '   ']]
gameover = [False, False]
tie = 0
taken = ()

# Setting names
names = set_name()

# First player x (true) or o (false)?
player1x = player1_x()

# Do you want to play?
gameon = game_on()

# Game duration
while gameover == [False, False]:

    if gameon:
        board, player_1_input, taken = player1_move(board, names, taken)
        display_board(board)
        tie += 1
        taken.append(player_1_input)
    else:
        print('Goodbye')
        break

    gameover = [x_win(board), o_win(board)]

    # Break loop if player 1 wins
    if gameover[0] or tie == 9:
        break

    board, player_2_input, taken = player2_move(board, names, taken)
    tie += 1
    taken.append(player_2_input)

    gameover = [x_win(board), o_win(board)]

    # Break loop if player 2 wins
    if gameover[1] or tie == 9:
        break

    display_board(board)

if gameover == [True, False]:
    print(f'{names[0]} wins!')
elif gameover == [False, True]:
    print(f'{names[1]} wins!')
else:
    print("It's a tie!")
