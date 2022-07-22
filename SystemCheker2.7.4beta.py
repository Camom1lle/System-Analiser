from tkinter import *
import tkinter as tk
from datetime import datetime
import os
import time
import psutil



root = tk.Tk()

def task(event):
    os.startfile('systemchek.exe')

def task1(event):
    for process in (process for process in psutil.process_iter() if process.name()=="System Cheker 2.7.4 beta.exe"):
        process.kill()

root["bg"] = "#649a9e"

root.geometry('600x400')

label1 = Label(text="Welcome to system cheker \n\n", fg="#1f4447", bg="#649a9e",font="20")
label1.pack()
 
poetry = "Thank you for using my software\n Made by Zhukov Roman"
label2 = Label(text=poetry,
            justify=CENTER,
            fg="#1f4447",
            bg="#649a9e")

label2.place(relx=.1,
            rely=.8)

btn = Button(text="Get Info",       # текст кнопки 
            background="#1f4447",     # фоновый цвет кнопки
            foreground="#65baba",     # цвет текста
            padx="20",             # отступ от границ до содержимого по горизонтали
            pady="8",              # отступ от границ до содержимого по вертикали
            font="14",              
             )
btn.place(relx=0.5, rely=0.5, anchor=CENTER)
btn.bind('<Button-1>', task)
btn.pack()

btn1 = Button(text="QUIT",       # текст кнопки 
            background="#1f4447",     # фоновый цвет кнопки
            foreground="#65baba",     # цвет текста
            padx="20",             # отступ от границ до содержимого по горизонтали
            pady="8",              # отступ от границ до содержимого по вертикали
            font="14",              
             )
btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
btn1.bind('<Button-1>', task1)
btn1.pack()

root.title("System Cheker 2.7.3 beta")
root.mainloop()