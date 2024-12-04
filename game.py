from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("Tick Tack Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tick Tack Toe", font=("Arial", 20), fg="yellow", bg="black")
titleLabel.pack()

frame2 = Frame(root)
frame2.pack()

board = {}
for i in range(1, 10):
    board[i] = ""

turn = "x"

def checkResult():
    global board

    winning_combinations = [
        (1, 2, 3),  
        (4, 5, 6),  
        (7, 8, 9),  
        (1, 4, 7),  
        (2, 5, 8),  
        (3, 6, 9),  
        (1, 5, 9),  
        (3, 5, 7),  
    ]
    
    
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != "":
            messagebox.showinfo("Game Over", f"Player '{board[combo[0]]}' wins!")
            resetGame()
            return

    
    if all(board[pos] != "" for pos in board):
        messagebox.showinfo("Game Over", "It's a tie!")
        resetGame()


def resetGame():
    global board, turn
    turn = "x"
    for pos in board:
        board[pos] = ""
    for button in frame2.winfo_children():
        button["text"] = " "


def play(event):
    global turn
    button = event.widget
    clicked = int(button._name[-1])
    
    if button["text"] == " ":
        if turn == "x":
            button["text"] = "X"
            turn = "o"
            board[clicked] = "x"
        else:
            button["text"] = "O"
            turn = "x"
            board[clicked] = "o"
    checkResult()


for i in range(3):
    for j in range(3):
        button_id = i * 3 + j + 1  
        button = Button(frame2, text=" ", width=4, height=2, font=("Arial", 30), name=f"button{button_id}")
        button.grid(row=i, column=j)
        button.bind("<Button-1>", play)

root.mainloop()


