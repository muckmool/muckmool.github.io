from tkinter import *
import tkinter.ttk as ttk

app = Tk()

def changing_color(_):
     new.configure(bg="red")

def new_window():
     global new
     new = Toplevel()
     #new.bind("<Button-1>", changing_color)

making_window_btn = Button(app, text="새창만들기", command=new_window)
making_window_btn.pack(pady="5")

app.title('main')
app.geometry("300x300")

app.mainloop()