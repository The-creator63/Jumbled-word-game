from tkinter import*
import random
from tkinter import messagebox

root = Tk()
root.geometry("500x500+500+150")
root.title("Jumble word game")
root.configure(background = "black")

Label(root,text = "JUMBLED WORD GAME",bg = "black",fg = "white",font = ("Times",30,"bold")).pack(pady = 5)
word_lbl = Label(root,bg = "black",fg = "red",font = ("Times",20,"bold"))
word_lbl.pack(pady = 30,ipady = 10, ipadx = 10)
ans = StringVar()
answer = Entry(root,textvariable = ans,width = 30)
answer.pack(ipadx = 5,ipady = 5)
Button(root,text = "CHECK",bg = "yellow",fg = "green",font = ("Times",20,"bold"),relief = GROOVE,width = 10).pack(pady = 40)
Button(root,text = "RESET",bg = "blue",fg = "red",font = ("Times",20,"bold"),relief = GROOVE,width = 10).pack(pady = 40)
root.mainloop()