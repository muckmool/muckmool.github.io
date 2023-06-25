import json

try:
    import Tkinter as tk
except:
    import tkinter as tk
    
import time
import pyperclip

from tkinter import *            # tkinter 라이브러리에 모든 함수를 사용하겠다.



def search_hanja(): 
        with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        global g_data

        g_data = data

        max = len(g_data['dictionary'])

        global temp2

        temp2 = pyperclip.paste()

        temp2 = temp2[0:20]

        temp4 = "없음"

        for i in range(max):
            if(temp2 == g_data['dictionary'][i]['hanja'] or temp2 == g_data['dictionary'][i]['hangul'] or temp2 == g_data['dictionary'][i]['japan'] or temp2 == g_data['dictionary'][i]['exp']):
                temp4 = g_data['dictionary'][i]['hanja']
                break      
            else: 
                i = i + 1

        return temp4


def search_hangul(): 

        max = len(g_data['dictionary'])

        #temp2 = pyperclip.paste()

        temp4 = "없음"

        for i in range(max):
            if(temp2 == g_data['dictionary'][i]['hanja'] or temp2 == g_data['dictionary'][i]['hangul'] or temp2 == g_data['dictionary'][i]['japan'] or temp2 == g_data['dictionary'][i]['exp']):
                temp4 = g_data['dictionary'][i]['hangul']
                break      
            else: 
                i = i + 1

        return temp4



def search_japan(): 

        max = len(g_data['dictionary'])

        #temp2 = pyperclip.paste()

        temp4 = "없음"

        for i in range(max):
            if(temp2 == g_data['dictionary'][i]['hanja'] or temp2 == g_data['dictionary'][i]['hangul'] or temp2 == g_data['dictionary'][i]['japan'] or temp2 == g_data['dictionary'][i]['exp']):
                temp4 = g_data['dictionary'][i]['japan'] + " "+ g_data['dictionary'][i]['exp']
                break      
            else: 
                i = i + 1

        return temp4


def search_china(): 

        max = len(g_data['dictionary'])

        #temp2 = pyperclip.paste()

        temp4 = "없음"

        for i in range(max):
            if(temp2 == g_data['dictionary'][i]['hanja'] or temp2 == g_data['dictionary'][i]['hangul'] or temp2 == g_data['dictionary'][i]['japan'] or temp2 == g_data['dictionary'][i]['exp']):
                temp4 = g_data['dictionary'][i]['china']
                break      
            else: 
                i = i + 1

        return temp4


def search_english(): 

        max = len(g_data['dictionary'])

        #temp2 = pyperclip.paste()

        temp4 = "없음"

        for i in range(max):
            if(temp2 == g_data['dictionary'][i]['hanja'] or temp2 == g_data['dictionary'][i]['hangul'] or temp2 == g_data['dictionary'][i]['japan'] or temp2 == g_data['dictionary'][i]['exp']):
                temp4 = g_data['dictionary'][i]['english']
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
        self.root.geometry("561x71-10-450")       # 창 크기설정
        self.root.title("dictionary")    # 창 제목설정
        self.root.option_add("*Font","맑은고딕 15") # 폰트설정
        self.root.resizable(False, False)  # x, y 창 크기 변경 불가

        self.ent00 = Entry(self.root, width=25)
        self.ent01 = Entry(self.root, width=25)

        self.ent10 = Entry(self.root, width=25)
        self.ent11 = Entry(self.root, width=25)

        self.ent20 = Entry(self.root, width=25)
        self.ent21 = Entry(self.root, width=25)
        #self.ent31 = Entry(self.root, width=40)


        self.ent00.grid(row=0,column=0)
        self.ent01.grid(row=0,column=1)

        self.ent10.grid(row=1,column=0)
        self.ent11.grid(row=1,column=1)

        self.ent20.grid(row=2,column=0)
        self.ent21.grid(row=2,column=1)
        #self.ent31.grid(row=3,column=1)




        self.update_clock()
        self.root.mainloop()

    global l_check, temp99
    l_check = ""
    temp99 = ""

    def update_clock(self):
        #now = time.strftime("%H:%M:%S")
        

        global l_check, temp99

        try:
                l_check = pyperclip.paste()
        except: 
                print("클립보드에러")

                
        if(l_check != temp99):
            #self.label0.configure(text=now)

            temp99 = l_check

            self.ent00.delete(0, "end")
            self.ent00.insert(0, temp99)

            self.ent01.delete(0, "end")
            self.ent01.insert(0, search_hanja())

            self.ent10.delete(0, "end")
            self.ent10.insert(0, search_japan())

            self.ent11.delete(0, "end")
            self.ent11.insert(0, search_china())

            self.ent20.delete(0, "end")
            self.ent20.insert(0, search_hangul())

            self.ent21.delete(0, "end")
            self.ent21.insert(0, search_english())


        #self.ent31.delete(0, "end")
        #self.ent31.insert(0, now)

                
        self.root.after(1000, self.update_clock)

app=Clock()