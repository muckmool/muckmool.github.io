from tkinter import *

window = None

canvas = None

x1, y1 = None, None

x0, y0 = 0, 0


# 붓글씨
tx0, ty0, tx1, ty1 = 5, 5, 5, 5

# 네이밍펜
#tx0, ty0, ty1, ty2 = 2, 2, 2, 2 

# 싸인펜
#tx0, ty0, ty1, ty2 = 1, 1, 1, 1 


def change_boot():
    global tx0, ty0, tx1, ty1
    tx0, ty0, tx1, ty1 = 5, 5, 5, 5

def change_name():
    global tx0, ty0, tx1, ty1
    tx0, ty0, tx1, ty2 = 2, 2, 2, 2

def change_sign():
    global tx0, ty0, tx1, ty1
    tx0, ty0, tx1, ty2 = 1, 1, 1, 1



def mouseMove(event):
    global x1, y1, x0, y0
    x1 = event.x
    y1 = event.y
    if(x0 is not 0 and y0 is not 0):
        #canvas.create_line(x0, y0, x1, y1, fill="black", width = 1)
        canvas.create_oval(x0-tx0, y0-ty0, x1+tx1, y1+ty1, fill="black")
    x0 = event.x
    y0 = event.y
   

def buttonReleased(event):
    global x0, y0
    x0 = 0
    y0 = 0



def clearCanvas():
    canvas.delete("all")

window=Tk()

frame = Frame(window)


frame.pack()


canvas=Canvas(window, height=1000,width=1800)


canvas.bind('<B1-Motion>', mouseMove)

canvas.bind('<ButtonRelease-1>', buttonReleased)


canvas.pack(side=BOTTOM)


window.title("Paint")


clear = Button(frame, text="Clear", fg = "red", command=clearCanvas)

#clear.pack(side=BOTTOM)

clear.grid(row=1, column = 1)

boot1 = Button(frame, text="붓펜",command=change_boot)

boot1.grid(row=1, column = 2)

name1 = Button(frame, text="네임펜",command=change_name)

name1.grid(row=1, column = 3)

sign1 = Button(frame, text="싸인펜",command=change_sign)

sign1.grid(row=1, column = 4)



window.mainloop()