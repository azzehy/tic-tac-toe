# Initialize the board as a list of 9 empty spaces
board=["-","-","-",
       "-","-","-",
       "-","-","-"]

# Set the starting player to "X"
player = "X"

# Variable to track the winner
winner = None

# Variable to keep the game running
game_active  =True




# Function to display the board
def print_board(board):
    print("+---+---+---+")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("+---+---+---+")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("+---+---+---+")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("+---+---+---+")


# Function to get a valid player input
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

# Function to validate if a move is legal
def validate_move(board,val):       
    while board[val-1] != "-":  # Check if the position is already taken
        print("Full")
        val = get_player_input()
    board[val-1] = player   # Assign the player's symbol to the board




# Function to check for a vertical win
def check_vertical(board):
    global winner
    if (board[0] == board[3] == board[6] and board[0] != "-") or \
       (board[1] == board[4] == board[7] and board[1] != "-") or \
       (board[2] == board[5] == board[8] and board[2] != "-"):
        winner=player
        return True

# Function to check for a horizontal win
def check_horizontal(board):
    global winner
    if (board[0] == board[1] == board[2] and board[0] != "-") or \
       (board[3] == board[4] == board[5] and board[3] != "-") or \
       (board[6] == board[7] == board[8] and board[6] != "-"):
        winner=player
        return True

# Function to check for a diagonal win
def diagonal(board):
    global winner
    if (board[0]==board[4]==board[8] and board[0]!="-") or (board[2] == board[4] == board[6] and board[2] != "-") :
        winner=player
        return True

# Function to check if the game is a tie
def check_tie(board):
    global game_active
    if "-" not in board:
        print_board(board)
        print("sThe game is a tie!")
        game_active = False

# Function to check if there's a winner
def check_winner():
    global game_active
    if check_vertical(board) or check_horizontal(board) or diagonal(board):
        print(f"player {winner} is the winner")
        game_active=False
        return True

# Function to switch the turn to the other player
def switch_player():
    global player
    if player=="X":
        player="O"
    else:
        player="X"

# Main game loop
while game_active:
    print_board(board)  # Print the current board state
    posi = get_player_input()   # Get player input
    validate_move(board, posi)  # Validate and place the move
    if(check_winner()): # Check if there is a winner
        print_board(board)  # Display the final board
        break
    check_tie(board)    # Check if the game ended in tie
    switch_player() # Switch to the next player