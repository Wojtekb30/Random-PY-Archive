import os
from tkinter import *
import tkinter.messagebox
import tkinter
print("Program wymaga ESpeak i dziala tylko na Linux")
print("This program requires ESpeak and works only on Linux")
print("-Wojtekb30, Bird Tech, 27.02.2022")

def readd():
    wybor = str(wpisz.get())
    jezyk = str(lbl.curselection())
    if jezyk == "(0,)":
        os.system('espeak -v pl '+'"'+wybor+'"')
    if jezyk == "(1,)":
        os.system('espeak -v en '+'"'+wybor+'"')
    if jezyk == "(2,)":
        os.system('espeak -v fr '+'"'+wybor+'"')          
    if jezyk == "(3,)":
        os.system('espeak -v de '+'"'+wybor+'"')
    if jezyk == "(4,)":
        os.system('espeak -v es '+'"'+wybor+'"')
    if jezyk == "(5,)":
        os.system('espeak -v it '+'"'+wybor+'"')


top = tkinter.Tk()
top.title("WojSpeech")
top.resizable(width=False, height=False)


lbl = Listbox(top)
lbl.insert(1, "Polski")
lbl.insert(2, "English")
lbl.insert(3, "French")
lbl.insert(4, "German")
lbl.insert(5, "Spanish")
lbl.insert(6, "Italian")

lbl.pack()
wpisz = tkinter.Entry(top)
wpisz.pack()
btn =tkinter.Button(top, text ="Read", command = readd)
btn.pack()
top.mainloop()
