import tkinter as tk
from tkinter import messagebox

# Tic-Tac-Toe board
board = ["-"] * 9
player = "X"
game_active = True

# Create GUI window
root = tk.Tk()
root.title("Tic-Tac-Toe - Two Players")
root.configure(bg="#2C3E50")

# Buttons for the game board
buttons = []

# Function to check for a winner
def check_winner():
    global game_active
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] and board[condition[0]] != "-":
            winner = board[condition[0]]
            for i in condition:
                buttons[i].config(bg="#1ABC9C")  # Highlight winning moves
            messagebox.showinfo("Game Over", f"Player {winner} wins!")
            game_active = False
            return True
    
    if "-" not in board:
        messagebox.showinfo("Game Over", "It's a Tie!")
        game_active = False
        return False
    
    return False

# Function to handle player moves
def make_move(index):
    global player
    if board[index] == "-" and game_active:
        board[index] = player
        buttons[index].config(text=player, state=tk.DISABLED, fg="white", bg="#3498DB" if player == "X" else "#E74C3C")
        
        if check_winner():
            return

        # Switch players
        player = "O" if player == "X" else "X"

# Function to reset the game
def reset_game():
    global board, player, game_active
    board = ["-"] * 9
    player = "X"
    game_active = True
    for button in buttons:
        button.config(text="", state=tk.NORMAL, bg="#ECF0F1")

# Create the buttons for the board
for i in range(9):
    button = tk.Button(root, text="", font=("Arial", 24, "bold"), height=2, width=5, bg="#ECF0F1", fg="black", 
                       relief=tk.RAISED, command=lambda i=i: make_move(i))
    button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
    buttons.append(button)

# Reset button
reset_button = tk.Button(root, text="Restart Game", font=("Arial", 14, "bold"), bg="#F39C12", fg="white", 
                         command=reset_game, relief=tk.RAISED)
reset_button.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()
