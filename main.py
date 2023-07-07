from tkinter import *
import random


def next_t(row, col):
    global player
    if button[row][col]['text'] == "" and winner() is False:
        if player == players[0]:
            button[row][col]['text'] = player
            if winner() is False:
                player = players[1]
                label.config(text=players[1] + "'s turn")
            elif winner() is True:
                label.config(text=players[0] + " wins!")
            elif winner() == "Draw":
                label.config(text="Draw!")
        else:
            button[row][col]['text'] = player
            if winner() is False:
                player = players[0]
                label.config(text=players[0] + "'s turn")
            elif winner() is True:
                label.config(text=players[1] + " wins!")
            elif winner() == "Draw":
                label.config(text="Draw!")



def winner():
    for row in range(3):
        if button[row][0]['text'] == button[row][1]['text'] == button[row][2]['text'] != "":
            button[row][0].config(fg="#1d1238", bg="#5636a7")
            button[row][1].config(fg="#1d1238", bg="#5636a7")
            button[row][2].config(fg="#1d1238", bg="#5636a7")
            return True
    for col in range(3):
        if button[0][col]['text'] == button[1][col]['text'] == button[2][col]['text'] != "":
            button[0][col].config(fg="#1d1238", bg="#5636a7")
            button[1][col].config(fg="#1d1238", bg="#5636a7")
            button[2][col].config(fg="#1d1238", bg="#5636a7")
            return True
    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != "":
        button[0][0].config(fg="#1d1238", bg="#5636a7")
        button[1][1].config(fg="#1d1238", bg="#5636a7")
        button[2][2].config(fg="#1d1238", bg="#5636a7")
        return True
    elif button[2][0]['text'] == button[1][1]['text'] == button[0][2]['text'] != "":
        button[2][0].config(fg="#1d1238", bg="#5636a7")
        button[1][1].config(fg="#1d1238", bg="#5636a7")
        button[0][2].config(fg="#1d1238", bg="#5636a7")
        return True
    elif empty_buttons() is True:
        return "Draw"
    else:
        return False


def empty_buttons():
    empty_buttons = 9

    for row in range(3):
        for col in range(3):
            if button[row][col]['text'] != "":
                empty_buttons -= 1
    if empty_buttons == 0:
        for row in range(3):
            for col in range(3):
                button[row][col].config(bg="#ff0000")
        return True
    else:
        return False


def new_game():
    global player
    player = random.choice(players)
    for row in range(3):
        for col in range(3):
            button[row][col].config(text="", fg="black", bg="white")
window = Tk()
window.geometry("600x680")
window.title("Tic Tac Toe Solo")
window.resizable(False, False)
players = ['x', 'o']
player = random.choice(players)

button = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

label = Label(window, text=player + "'s turn", font=("Comic Sans", 40))
label.pack()

frame = Frame(window)
frame.pack()

for row in range(3):
    for col in range(3):
        button[row][col] = Button(frame, text='', font=("Comic Sans", 30), height=3, width=6,
                                  bg="white", fg="black", activeforeground="black", activebackground="white",
                                  command=lambda row=row, col=col: next_t(row, col))
        button[row][col].grid(row=row, column=col)

restart = Button(frame, text="restart", font=("Comic Sans", 30), command=new_game)
restart.grid(row=4, columnspan=3)
window.mainloop()

