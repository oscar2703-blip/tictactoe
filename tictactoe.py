from tkinter import*
import random
from tkinter import messagebox
from functools import partial
from copy import deepcopy

sign = 0

#creating an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]
print(board)

def winner(b, l):
    return(
        # horizontal wins:
        (b[0][0]==1 and b[0][1]==1 and b[0][2]==1) or
        (b[1][0]==1 and b[1][1]==1 and b[1][2]==1) or
        (b[2][0]==1 and b[2][1]==1 and b[2][2]==1) or
        # vertical wins:
        (b[0][0]==1 and b[1][0]==1 and b[2][0]==1) or
        (b[0][1]==1 and b[1][1]==1 and b[2][1]==1) or
        (b[0][2]==1 and b[1][2]==1 and b[2][2]==1) or
        # diagonal wins:
        (b[0][0]==1 and b[1][1]==1 and b[2][2]==1) or
        (b[0][2]==1 and b[1][1]==1 and b[2][0]==1)
    )

def get_text(i,j,gb,l1,l2):
    global sign
    if board[i][j] == " ":
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = 'X'
        else:
            l1.config(state= ACTIVE)
            l2.config(state = DISABLED)
            board[i][j] = "O"
        sign+=1
        button[i][j].config(text=board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("winner", "player 1 won the match")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("winner","player 2 won the match")
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("tie", "there is a tie")

def isfull():
    flag = True
    for i in board():
        if i.count(' ') > 0:
            flag = False
    return flag

def isfree(i,j):
    return board[i][j] == " "

#For multiplayer
# creating GUI of gb to play with another player
def gameboard_pl(game_board, l1, l2):
    global button 
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            # creating and configuring the buttons
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd=5, bg="cyan", fg="turquoise", command=get_t, height=4, width=4)
            button[i][j].grid(row=m, column= n)
    game_board.mainloop()
                    