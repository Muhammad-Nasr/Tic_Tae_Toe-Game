from tkinter import *
from tkinter import messagebox


COLOR='#14bdac'
FONT_TITLE = ("Arial", 20, "italic")
FONT_TEXT = "Arial", 60, "bold"


# variables for the game

cells_winning= ['abc', 'adg', 'aei', 'beh', 'cfi', 'ceg', 'def', 'ghi']
clicked = TRUE
count = 0
playerX = []
playerO = []

playerX_cell= ""
playerO_cell = ""


## create function for buttons
def click(b, cell):
    global cells_winnig, clicked, count, playerX, playerO, playerX_cell, playerO_cell

    if b['text'] == '' and clicked:

        b.config(text='X')
        b.config(state='disabled')

        playerX_cell += cell
        playerX .append(b)

        clicked = False
        count += 1
        winner(count= count, cells= playerX_cell, player= playerX)

    elif b['text'] == '' and clicked == False:

        b.config(text= 'O')
        b.config(state='disabled')

        count += 1
        playerO.append(b)
        playerO_cell += cell

        winner(count=count, cells=playerO_cell, player=playerO)

        clicked = TRUE


## create function to check winner

def winner(count, cells, player):

    if count != 9:
        if cells in cells_winning:
            for button in player:
                btn = button
                btn.config(bg= 'red')
            messagebox.showinfo(title="Congratulations", message=" You are the winner!! kudos")

    else:
        messagebox.showinfo(message=" The game is draw! good luck next time.")



# create my windows

window= Tk(screenName='Tic-Tac-Toe')
window.title('Tic Game')

window.config(padx=20, pady=20, bg=COLOR)


# create buttons

b1 = Button(window, font= FONT_TITLE,  width=3, height=3, bg=COLOR, command=lambda:click(b1, 'a'))
b2 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b2, 'b'))
b3 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b3, 'c'))

b4 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b4, 'd'))
b5 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b5, 'e'))
b6 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b6, 'f'))

b7 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b7, 'g'))
b8 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b8, 'h'))
b9 = Button(window, font= FONT_TITLE, width=3, height=3, bg=COLOR, command=lambda:click(b9, 'i'))

b1.grid(row=0, column=4)
b2.grid(row=0, column=5)
b3.grid(row=0, column=6)

b4.grid(row=1, column=4)
b5.grid(row=1, column=5)
b6.grid(row=1, column=6)

b7.grid(row=2, column=4)
b8.grid(row=2, column=5)
b9.grid(row=2, column=6)



window.mainloop()
