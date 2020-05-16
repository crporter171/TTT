# Tic-Tac Toe

# The actual board...
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# Game is running and has not been completed yet
running = True

champion = None

current = "X"

# Display the gane board
def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

# Handle the turn system
def turn(current):
    print(current + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            position = input("Invalid input: Choose a position from 1-9: ")
        position = int(position)-1

        if board[position] == "-":
            valid = True
        else:
            print("Spot taken, try again.")

    board[position] = current
    display()

def play():
    global champion
    display()
    while running:
        turn(current)
        if_game_over()
        switch()
    # Game has ended printing the winner
    if champion == "X" or champion == "O":
        print(champion + " won!")
    elif champion == None:
        print("Tie")

def if_game_over():
    check_win()
    check_tie()

def check_win():
    global champion
    row_win = check_row()
    col_win = check_column()
    dia_win = check_diagnal()
    if row_win:
        champion = row_win
    elif col_win:
        champion = col_win
    elif dia_win:
        champion = dia_win
    return

def check_row():
    global running
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        running = False
    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

def check_column():
    global running
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        running = False
    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]

def check_diagnal():
    global running
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[2] == board[4] == board[6] != "-"
    if dia_1 or dia_2:
        running = False
        return board[4]

def check_tie():
    global running
    if "-" not in board:
        running = False
    return

def switch():
    global current
    if current == "X":
        current = "O"
    else:
        current = "X"
    return

play()
