import json
from tkinter import *
import tkinter.font
import time
import pyperclip
import sys


tk = Tk()
tk.geometry("460x260+1150+700")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('사전')
tk.wm_attributes("-topmost", 1)


def new():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['hangul'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{ "hangul": "X", "hanja": ".", "english": ".", "china": ".", "china_s": ".", "japan_k": ".", "japan_m": ".", "japan_s": "."}'

        string = string + '\n]}'

        #print(string)

        f = open("data13.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry01.get()
    result = -1

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp ):
            result = i
            break
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['english'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['china'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['china_s'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['japan_k'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['japan_m'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['japan_s'])


def copy():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['hangul'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{ "hangul": "X", "hanja": ".", "english": ".", "china": ".", "china_s": ".", "japan_k": ".", "japan_m": ".", "japan_s": "."}'

        string = string + '\n]}'

        #print(string)

        f = open("data13.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry01.get()
    result = -1

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp ):
            result = i
            break
    
    entry00.delete(0,"end")
    entry00.insert(0,result)



def update():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    seq = int(entry00.get())

    save_trigger = FALSE

    if(seq>-1 and seq<max):
        save_trigger = TRUE
        data['dictionary'][seq]['hangul'] = entry1.get()
        data['dictionary'][seq]['hanja'] = entry2.get()
        data['dictionary'][seq]['english'] = entry31.get()
        data['dictionary'][seq]['china'] = entry41.get()
        data['dictionary'][seq]['china_s'] = entry51.get()
        data['dictionary'][seq]['japan_k'] = entry61.get()
        data['dictionary'][seq]['japan_m'] = entry71.get()
        data['dictionary'][seq]['japan_s'] = entry81.get()


    if(save_trigger == TRUE):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("data13.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()

        entry00.delete(0,"end")
        entry00.insert(0, seq)
        entry01.delete(0,"end")
        entry01.insert(0, "업뎃완료")
        
        



def search_hangul():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry91.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")


    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp or data['dictionary'][i]['hanja'] == h_temp or data['dictionary'][i]['china'] == h_temp or data['dictionary'][i]['china_s'] == h_temp or data['dictionary'][i]['japan_k'] == h_temp or data['dictionary'][i]['japan_m'] == h_temp  or data['dictionary'][i]['japan_s'] == h_temp):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            entry00.insert(0,result)
            entry1.insert(0,data['dictionary'][i]['hangul'])
            entry2.delete(0,"end")
            entry2.insert(0,data['dictionary'][i]['hanja'])
            entry31.delete(0,"end")
            entry31.insert(0,data['dictionary'][i]['english'])
            entry41.delete(0,"end")
            entry41.insert(0,data['dictionary'][i]['china'])
            entry51.delete(0,"end")
            entry51.insert(0,data['dictionary'][i]['china_s'])
            entry61.delete(0,"end")
            entry61.insert(0,data['dictionary'][i]['japan_k'])
            entry71.delete(0,"end")
            entry71.insert(0,data['dictionary'][i]['japan_m'])
            entry81.delete(0,"end")
            entry81.insert(0,data['dictionary'][i]['japan_s'])
            break

 


def next():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    result = int(entry00.get()) + 1

    if(result >= max): 
        result = result - 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['english'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['china'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['china_s'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['japan_k'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['japan_m'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['japan_s'])


def previous():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    result = int(entry00.get()) - 1

    if(result < 0): 
        result = result + 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['english'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['china'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['china_s'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['japan_k'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['japan_m'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['japan_s'])


def search_seq():
    with open ("data13.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    result = max - 1

    if(entry00.get() != ''):
        result = int(entry00.get())

    if(result<0):
        result = 0

    if(result >= max): 
        result = result - 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['english'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['china'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['china_s'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['japan_k'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['japan_m'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['japan_s'])


global l_check, temp99
l_check = ""
temp99 = ""


def clock(): # 현재 시간 표시 / 반복
    live_T = time.strftime("%H:%M:%S") # Real Time
    #entry1.delete(0,"end")
    #entry1.insert(0,live_T)

    global l_check, temp99

    l_check = pyperclip.paste()

    if(l_check != temp99):
        temp99 = l_check
        entry91.delete(0,"end")
        entry91.insert(0,temp99)
        search_hangul()
    
    tk.after(200, clock) # .after(지연시간{ms}, 실행함수)

    
label9 = Label(tk,text='조회', font=font1).grid(row=0, column=0)
label0 = Label(tk,text='SEQ', font=font1).grid(row=1, column=0)
label1 = Label(tk,text='한글', font=font1).grid(row=2, column=0)
label2 = Label(tk,text='한자', font=font1).grid(row=3,column=0)
label3 = Label(tk,text='영어', font=font1).grid(row=4,column=0)
label4 = Label(tk,text='중국', font=font1).grid(row=5,column=0)
label5 = Label(tk,text='병음', font=font1).grid(row=6,column=0)
label6 = Label(tk,text='칸지', font=font1).grid(row=7,column=0)
label7 = Label(tk,text='일훈', font=font1).grid(row=8,column=0)
label8 = Label(tk,text='일음', font=font1).grid(row=9,column=0)

# 각 단위 입력받는 부분 만들기
entry91 = Entry(tk, width=30, font=font1)
entry00 = Entry(tk, width=30, font=font1)
entry01 = Entry(tk, width=10, font=font1)
entry1 = Entry(tk, width=30, font=font1)
entry2 = Entry(tk, width=30, font=font1)

entry31 = Entry(tk, width=30, font=font1)
entry41 = Entry(tk, width=30, font=font1)
entry51 = Entry(tk, width=30, font=font1)
entry61 = Entry(tk, width=30, font=font1)
entry71 = Entry(tk, width=30, font=font1)
entry81 = Entry(tk, width=30, font=font1)


entry91.grid(row=0,column=1)
entry00.grid(row=1,column=1)
entry01.grid(row=1,column=2)
entry1.grid(row=2,column=1)
entry2.grid(row=3,column=1)

entry31.grid(row=4,column=1)
entry41.grid(row=5,column=1)
entry51.grid(row=6,column=1)
entry61.grid(row=7,column=1)
entry71.grid(row=8,column=1)
entry81.grid(row=9,column=1)

btn2 = Button(tk,text='조회',bg='black',fg='white',command=search_hangul).grid(row=0,column=2)
btn5 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq).grid(row=1,column=3)


btn1 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=3,column=3)

btn3 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=5,column=3)
btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=7,column=3)

btn4 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=9,column=2)
btn7 = Button(tk,text='복사',bg='black',fg='white',command=copy).grid(row=9,column=3)

clock()

tk.mainloop()









