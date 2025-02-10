board=["-","-","-",
       "-","-","-",
       "-","-","-"]
player="X"
winner=None
game_active=True




#design board
def print_board(board):
    print("+---+---+---+")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("+---+---+---+")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("+---+---+---+")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("+---+---+---+")


#dakhel
def get_player_input():
    while True:
        try:
            position=int(input("choose your position from 1->9: "))
            if position>=1 and position<=9:
                return position
                break
            else:
                print("Please enter a number within the range")
        except ValueError:
            print("Please enter a number")
def validate_move(board,val):       
    while board[val-1] != "-":
        print("Full")
        val = get_player_input()
    board[val-1] = player




#wach rabeh
def check_vertical(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or \
       (board[1] == board[4] == board[7] and board[1] != "-") or \
       (board[2] == board[5] == board[8] and board[2] != "-"):
        winner=player
        return True


def check_horizontal(board):
    global winner
    if (board[0]==board[1]==board[2] and board[0]!="-") or \
        (board[3] == board[4] == board[5] and board[3] != "-") or \
            (board[6] == board[7] == board[8] and board[6] != "-"):
        winner=player
        return True


def diagonal(board):
    global winner
    if (board[0]==board[4]==board[8] and board[0]!="-") or (board[2] == board[4] == board[6] and board[2] != "-") :
        winner=player
        return True


def check_tie(board):
    global game_active
    if "-" not in board:
        print_board(board)
        print("sThe game is a tie!")
        game_active = False


def check_winner():
    global game_active
    if check_vertical(board) or check_horizontal(board) or diagonal(board):
        print(f"player {winner} is the winner")
        game_active=False
        return True
#bedel noba
def switch_player():
    global player
    if player=="X":
        player="O"
    else:
        player="X"

#bissmilah
while game_active:
    print_board(board)
    posi=get_player_input()
    validate_move(board,posi)
    if(check_winner()):
        print_board(board)
        break
    check_tie(board)
    switch_player()