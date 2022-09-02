import json

try:
    import Tkinter as tk
except:
    import tkinter as tk
    
import time
import pyperclip

from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.



#f = open("dic_test.txt","r", encoding="utf-8")
#arr = f.read()
#arr = arr.replace("\n", "")
#arr = arr.split(',,, ')
#f.close()




def search2(): 
        with open ("data2.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hangul'] 
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hangul'] 
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hangul'] 
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hangul'] 
                    break      
                else: 
                    i = i + 1

        return temp4


def search11(): 
        with open ("data2.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()
        word = list(temp)
        temp4 = ""

        # 1-1글자 조회

        if(len(word) > 0):

            temp3 = word[0]

            temp4 = temp4 + temp3

            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = temp4 + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search12(): 
        with open ("data2.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()
        word = list(temp)
        temp4 = ""

        # 1-2글자 조회

        if(len(word) > 1):

            temp3 = word[1]

            temp4 = temp4 + temp3

            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = temp4 + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search13(): 
        with open ("data2.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()
        word = list(temp)
        temp4 = ""

        # 1-3글자 조회

        if(len(word) > 2):

            temp3 = word[2]

            temp4 = temp4 + temp3

            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = temp4 + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search14(): 
        with open ("data2.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])


        temp = pyperclip.paste()
        word = list(temp)
        temp4 = ""

        # 1-4글자 조회

        if(len(word) > 3):

            temp3 = word[3]

            temp4 = temp4 + temp3

            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = temp4 + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4


class Clock():
    def __init__(self):
        #self.root = tk.Tk()
        #self.root.wm_attributes("-topmost", 1)
        #self.root.geometry('310x160-70-130')

        self.root = Tk()                      # 창을 생성
        self.root.wm_attributes("-topmost", 1)
        self.root.geometry("600x160-70-130")       # 창 크기설정
        self.root.title("dictionary")    # 창 제목설정
        self.root.option_add("*Font","맑은고딕 12") # 폰트설정
        self.root.resizable(False, False)  # x, y 창 크기 변경 불가

        self.ent = Entry(self.root, width=73)                 # root라는 창에 입력창 생성
        self.ent.pack()                        # 입력창 배치
        self.ent1 = Entry(self.root, width=73)                 # root라는 창에 입력창 생성
        self.ent1.pack()                        # 입력창 배치


        #self.label0 = tk.Label(text="", font=('Helvetica', 10), fg='black')
        #self.label2 = tk.Label(text="조회결과", font=('Helvetica', 12), fg='black', wraplength = 300)
        self.label11 = tk.Label(text="조회결과", font=('Helvetica', 12), fg='black', wraplength = 300) 
        self.label12 = tk.Label(text="조회결과", font=('Helvetica', 12), fg='black', wraplength = 300) 
        self.label13 = tk.Label(text="조회결과", font=('Helvetica', 12), fg='black', wraplength = 300) 
        self.label14 = tk.Label(text="조회결과", font=('Helvetica', 12), fg='black', wraplength = 300)         

        #self.label0.place(x=0, y=0)
        #self.label2.place(x=0, y=40)
        self.label11.place(x=0, y=50)
        self.label12.place(x=0, y=75)
        self.label13.place(x=0, y=100)
        self.label14.place(x=0, y=125)


        self.update_clock()
        self.root.mainloop()

    global l_check, temp99
    l_check = ""
    temp99 = ""

    def update_clock(self):
        #now = time.strftime("%H:%M:%S")
        

        global l_check, temp99
        l_check = pyperclip.paste()
                
        if(l_check != temp99):
            #self.label0.configure(text=now)

            self.ent.delete(0, "end")
            self.ent.insert(0, l_check)

            #self.label2.configure(text=search2())

            self.ent1.delete(0, "end")
            self.ent1.insert(0, search2())
            

            self.label11.configure(text=search11())
            self.label12.configure(text=search12())
            self.label13.configure(text=search13())
            self.label14.configure(text=search14())
            temp99 = l_check
                        
        self.root.after(1000, self.update_clock)

app=Clock()