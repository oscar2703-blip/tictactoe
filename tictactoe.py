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
    for i in board:
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
            button[i][j] = Button(game_board, bd=5, bg="cyan", fg="black", command=get_t, height=4, width=4)
            button[i][j].grid(row=m, column= n)
    game_board.mainloop()
            
# tp play with PC
def pc():
    possilbemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                possilbemove.append([1,j])

    move = []
    if possilbemove == []:
        return
    else:
        for let in ['O', 'X']:
            if i in possilbemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[i]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possilbemove:
            if i in [[0,0],[0,2], [2,0], [2,2]]:
                corner.append(i)

        if len(corner) > 0:
            move = randint(0,len(corner)-1)
            return corner
            edge = []
        for i in possilbemove:
            if i in [[0,1], [1,0], [2,1], [1,2]]:
                edge.append(i)
        if  len(edge) > 0:
            move = randint(0, len(edge)-1)
            return edge[move]  

def get_text_pc(i, j,gb, l1, l2):
    global sign
    if board[i][j] == " ":
        if sign % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l1.config(state=ACTIVE)
            l2.config(state=DISABLED)
            board[i][j] = "O"
        sign +=1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("winner","Player won the match")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("winner","Computer won the match")
    elif(isfull()):
        gb.destroy()
        x= False
        box = messagebox.showinfo("winner", "There is a tie")
    if(x):
        if sign % 2 != 0:
            move = pc()
            button[move[0][move[1]]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
                

def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m=3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n=j
            button[i].append(j)

            get_t = partial(get_text_pc, i, j, l1, l2, game_board)
            button[i][j] = Button(game_board, bd=5, bg="red", fg="black", 
                                    command=get_t, width=4, height=4)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()

def withpc(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("tic tac toe")
    l1 = Button(game_board, text="Player 1: X")
    l2 = Button(game_board, text="Player 2: O")
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    gameboard_pc(game_board, l1, l2)
    

# iniyialize the game board to play with another player
def withplayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("tic tac toe")
    l1 = Button(game_board, text="Player 1: X")
    l2 = Button(game_board, text="Player 2 = O")
    l1.grid(row=1, column=1)
    l2.grid(row=2, column=1)
    gameboard_pl(game_board, l1, l2)

def play():
    menu = Tk()
    menu.geometry("500x500")
    wpl = partial(withplayer, menu)
    wpc = partial(withpc, menu)
    head = Button(menu, text="Welcome to TicTacToe", bg="blue", fg="cyan", 
                    activeforeground="purple", activebackground="green", bd=5)
    head.pack(side="top")

    button1 = Button(menu, text="Computer", bg="blue", fg="cyan",
                     activeforeground="purple", activebackground="green", bd=5, command=wpc)
    button1.pack(side="top")

    button2 = Button(menu, text="Multiplayer", bg="blue", fg="cyan", 
                    activeforeground="purple", activebackground="green", bd=5, command=wpl)
    button2.pack(side="top")

    exit = Button(menu, text="Exit Game", bg="blue", fg="cyan", 
                    activeforeground="purple", activebackground="green", bd=5, command=menu.quit)
    exit.pack(side="top")

    menu.mainloop()

# call main function
if __name__ == '__main__':
    play()
    
    
                    