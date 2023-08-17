import json
from tkinter import *
import tkinter.font
import time
import pyperclip
import sys
import atexit


tk = Tk()
tk.geometry("320x290+1290+130")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('사전')
tk.wm_attributes("-topmost", 1)



def new():

    new_string = '{ "hangul": "X", "hanja": ".", "exp": ".", "english": ".", "china": ".", "china_s": ".", "japan_k": ".", "japan_m": ".", "japan_s": "."}'

    add_json = json.loads(new_string)

    g_data['dictionary'].append(add_json)

    entry00.delete(0,"end")

    search_seq()

    entry01.delete(0,"end")
    entry01.insert(0,"신규완료")


def delete():

    if(entry00.get() != ''):
        target = int(entry00.get())

    g_data['dictionary'].pop(target)

    
    target = target - 1
    
    entry00.delete(0,target)

    search_seq()

    entry01.delete(0,"end")
    entry01.insert(0,"삭제완료")


def copy():
    hangul = entry1.get()
    hanja = entry2.get()
    exp = entry101.get()
    english = entry31.get()
    china = entry41.get()
    china_s = entry51.get()
    japan_k = entry61.get()
    japan_m = entry71.get()
    japan_s = entry81.get()

    new_string = '{ "hangul": "' + hangul + '", "hanja": "' + hanja +'", "exp": "' + exp + '", "english": "'+ english +'", "china": "'+ china +'", "china_s": "'+ china_s +'", "japan_k": "'+ japan_k +'", "japan_m": "'+ japan_m +'", "japan_s": "'+ japan_s + '" }'

    add_json = json.loads(new_string)

    g_data['dictionary'].append(add_json)

    entry00.delete(0,"end")

    search_seq()

    entry01.delete(0,"end")
    entry01.insert(0,"카피완료")



def update():
    seq = int(entry00.get())

    g_data['dictionary'][seq]['hangul'] = entry1.get()
    g_data['dictionary'][seq]['hanja'] = entry2.get()
    g_data['dictionary'][seq]['exp'] = entry101.get()
    g_data['dictionary'][seq]['english'] = entry31.get()
    g_data['dictionary'][seq]['china'] = entry41.get()
    g_data['dictionary'][seq]['china_s'] = entry51.get()
    g_data['dictionary'][seq]['japan_k'] = entry61.get()
    g_data['dictionary'][seq]['japan_m'] = entry71.get()
    g_data['dictionary'][seq]['japan_s'] = entry81.get()

    entry01.delete(0,"end")
    entry01.insert(0, "업뎃완료")


def search_hangul4():
    data = g_data

    max = len(data['dictionary'])
    h_temp = entry91.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry101.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")

    search_result = FALSE


    for i in range(0,max):
        search = data['dictionary'][i]['china']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['china_s']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['japan_k']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['japan_m']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['japan_s']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['english']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['exp']
        if h_temp in search: search_result = TRUE

        if(search_result == TRUE):
            result = i
            search_result = TRUE
            break

    if(search_result == TRUE):
        i = result
        search_result = TRUE
        entry01.delete(0,"end")
        entry01.insert(0,"조회완료")
        entry00.delete(0,"end")
        entry00.insert(0,result)
        entry1.insert(0,data['dictionary'][i]['hangul'])
        entry2.delete(0,"end")
        entry2.insert(0,data['dictionary'][i]['hanja'])
        entry101.delete(0,"end")
        entry101.insert(0,data['dictionary'][i]['exp'])
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


def search_hangul3():
    data = g_data2

    max = len(data['dictionary'])
    h_temp = entry91.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry101.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")


    search_result = FALSE


    for i in range(0,max):
        search = data['dictionary'][i]['china']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['japan']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['english']
        if h_temp in search: search_result = TRUE

        search = data['dictionary'][i]['exp']
        if h_temp in search: search_result = TRUE

        if(search_result == TRUE):
            result = i
            search_result = TRUE
            break

    if(search_result == TRUE):
        i = result
        entry01.delete(0,"end")
        entry01.insert(0,"조회완료")
        entry00.delete(0,"end")
        #entry00.insert(0,result)
        entry1.insert(0,data['dictionary'][i]['hangul'])
        entry2.delete(0,"end")
        entry2.insert(0,data['dictionary'][i]['hanja'])
        entry101.delete(0,"end")
        entry101.insert(0,data['dictionary'][i]['exp'])
        entry31.delete(0,"end")
        entry31.insert(0,data['dictionary'][i]['english'])
        entry41.delete(0,"end")
        entry41.insert(0,data['dictionary'][i]['china'])
        entry51.delete(0,"end")
        entry61.delete(0,"end")
        entry71.delete(0,"end")
        entry71.insert(0,data['dictionary'][i]['japan'])
        entry81.delete(0,"end")

    if(search_result == FALSE):
        search_hangul4()


def search_hangul2():
    data = g_data2

    max = len(data['dictionary'])
    h_temp = entry91.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry101.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")


    search_result = FALSE


    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp or data['dictionary'][i]['hanja'] == h_temp or data['dictionary'][i]['english'] == h_temp or data['dictionary'][i]['china'] == h_temp or data['dictionary'][i]['japan'] == h_temp):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            #entry00.insert(0,result)
            entry1.insert(0,data['dictionary'][i]['hangul'])
            entry2.delete(0,"end")
            entry2.insert(0,data['dictionary'][i]['hanja'])
            entry101.delete(0,"end")
            entry101.insert(0,data['dictionary'][i]['exp'])
            entry31.delete(0,"end")
            entry31.insert(0,data['dictionary'][i]['english'])
            entry41.delete(0,"end")
            entry41.insert(0,data['dictionary'][i]['china'])
            entry51.delete(0,"end")
            entry61.delete(0,"end")
            entry71.delete(0,"end")
            entry71.insert(0,data['dictionary'][i]['japan'])
            entry81.delete(0,"end")
            search_result = TRUE
            break
    
    if(search_result == FALSE):
        search_hangul3()


def search_hangul():
    data = g_data

    max = len(data['dictionary'])
    h_temp = entry91.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry101.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")

    search_result = FALSE

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp or data['dictionary'][i]['hanja'] == h_temp or data['dictionary'][i]['english'] == h_temp or data['dictionary'][i]['china'] == h_temp or data['dictionary'][i]['china_s'] == h_temp or data['dictionary'][i]['japan_k'] == h_temp or data['dictionary'][i]['japan_m'] == h_temp  or data['dictionary'][i]['japan_s'] == h_temp):
            result = i
            search_result = TRUE
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            entry00.insert(0,result)
            entry1.insert(0,data['dictionary'][i]['hangul'])
            entry2.delete(0,"end")
            entry2.insert(0,data['dictionary'][i]['hanja'])
            entry101.delete(0,"end")
            entry101.insert(0,data['dictionary'][i]['exp'])
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

    if(search_result == FALSE):
        search_hangul2()



def next():
    data = g_data

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
    entry101.delete(0,"end")
    entry101.insert(0,data['dictionary'][i]['exp'])
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
    data = g_data

    #max = len(data['dictionary'])
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
    entry101.delete(0,"end")
    entry101.insert(0,data['dictionary'][i]['exp'])
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
    data = g_data
    
    max = len(data['dictionary']) - 1

    result = max

    if(entry00.get() != ''):
        result = int(entry00.get())

    if(result<0):
        result = 0

    if(result > max): 
        result = max - 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry101.delete(0,"end")
    entry101.insert(0,data['dictionary'][i]['exp'])
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


def read():
    with open ("data_b_14.json", "r", encoding = 'utf-8') as f:
        data1 = json.load(f)

    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data2 = json.load(f)

    global g_data 
    
    g_data = data1

    global g_data2
    
    g_data2 = data2

    entry01.delete(0,"end")
    entry01.insert(0,"읽기완료")


def save():
    data = g_data

    #print(data['dictionary'][3])

    max = len(data['dictionary'])

    string =  '{ "dictionary": [\n'

    for i in range(0,max):
        temp = data['dictionary'][i]
        temp = json.dumps(temp, ensure_ascii=False)
        string = string + temp + ',\n'

    string = string[:-2]

    string = string + '\n]}'

    #print(max)

    f = open("data_b_14.json", 'w', encoding = 'utf-8')
    f.write(string)
    f.close()

    #entry00.delete(0,"end")
    #entry00.insert(0, seq)
    entry01.delete(0,"end")
    entry01.insert(0, "저장완료")


def quit():
    save()
    tk.quit()


global l_check, temp99
l_check = ""
temp99 = ""


def clock(): # 현재 시간 표시 / 반복
    live_T = time.strftime("%H:%M:%S") # Real Time
    #entry1.delete(0,"end")
    #entry1.insert(0,live_T)

    global l_check, temp99

    l_check = pyperclip.paste()

    l_check = l_check[0:20]

    #print(chkvar.get())

    if(chkvar.get() == 0): 
        
        if( l_check != temp99):
            temp99 = l_check
            entry91.delete(0,"end")
            entry91.insert(0,temp99)
            search_hangul()
    
    tk.after(200, clock) # .after(지연시간{ms}, 실행함수)

    
label9 = Label(tk,text='조회', font=font1).grid(row=0, column=0)
label0 = Label(tk,text='SEQ', font=font1).grid(row=1, column=0)
label1 = Label(tk,text='한글', font=font1).grid(row=2, column=0)
label2 = Label(tk,text='한자', font=font1).grid(row=3,column=0)
label_10 = Label(tk,text='설명', font=font1).grid(row=4,column=0)
label3 = Label(tk,text='영어', font=font1).grid(row=5,column=0)
label4 = Label(tk,text='중국', font=font1).grid(row=6,column=0)
label5 = Label(tk,text='병음', font=font1).grid(row=7,column=0)
label6 = Label(tk,text='칸지', font=font1).grid(row=8,column=0)
label7 = Label(tk,text='일훈', font=font1).grid(row=9,column=0)
label8 = Label(tk,text='일음', font=font1).grid(row=10,column=0)

# 각 단위 입력받는 부분 만들기
entry91 = Entry(tk, width=20, font=font1)
entry00 = Entry(tk, width=20, font=font1)
entry01 = Entry(tk, width=6, font=font1)
entry1 = Entry(tk, width=20, font=font1)
entry2 = Entry(tk, width=20, font=font1)
entry101 = Entry(tk, width=20, font=font1)

entry31 = Entry(tk, width=20, font=font1)
entry41 = Entry(tk, width=20, font=font1)
entry51 = Entry(tk, width=20, font=font1)
entry61 = Entry(tk, width=20, font=font1)
entry71 = Entry(tk, width=20, font=font1)
entry81 = Entry(tk, width=20, font=font1)



chkvar = IntVar()                             # chkvar에 int 형으로 값을 저장
chkbox = Checkbutton(tk, variable=chkvar)   # root라는 창에 체크박스 생성
chkbox.grid(row=3,column=2)


entry91.grid(row=0,column=1)
entry00.grid(row=1,column=1)
entry01.grid(row=1,column=2)
entry1.grid(row=2,column=1)
entry2.grid(row=3,column=1)
entry101.grid(row=4,column=1)

entry31.grid(row=5,column=1)
entry41.grid(row=6,column=1)
entry51.grid(row=7,column=1)
entry61.grid(row=8,column=1)
entry71.grid(row=9,column=1)
entry81.grid(row=10,column=1)


btn2 = Button(tk,text='조회',bg='black',fg='white',command=search_hangul).grid(row=0,column=2)
btn8 = Button(tk,text='저장',bg='black',fg='white',command=save).grid(row=0,column=3)
btn5 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq).grid(row=2,column=3)


btn1 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=4,column=3)

btn10 = Button(tk,text='read',bg='black',fg='white',command=read).grid(row=6,column=2)
btn3 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=6,column=3)
btn9 = Button(tk,text='삭제',bg='black',fg='white',command=delete).grid(row=8,column=2)
btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=8,column=3)

btn4 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=10,column=2)
btn7 = Button(tk,text='복사',bg='black',fg='white',command=copy).grid(row=10,column=3)

atexit.register(quit)

read()

clock()

tk.mainloop()









