import json
from tkinter import *
import tkinter.font


tk = Tk()
tk.geometry("900x340+700+600")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('사전')
tk.wm_attributes("-topmost", 1)


def new():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['hangul'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{ "hangul": "X", "hanja": ".", "h1": ".", "c1": ".", "h2": ".", "c2": ".", "h3": ".", "c3": ".", "h4": ".", "c4": ".", "h5": ".", "c5": ".", "h6": ".", "c6": ".", "exp":".", "china":".", "japan":"." }'

        string = string + '\n]}'

        #print(string)

        f = open("data2.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data2.json", "r", encoding = 'utf-8') as f:
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
    #entry1.delete(0,"end")
    #entry1.insert(0,data['dictionary'][i]['hangul'])
    #entry2.delete(0,"end")
    #entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['h1'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['h2'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['h3'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['h4'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['h5'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['h6'])
    entry32.delete(0,"end")
    entry32.insert(0,data['dictionary'][i]['c1'])
    entry42.delete(0,"end")
    entry42.insert(0,data['dictionary'][i]['c2'])
    entry52.delete(0,"end")
    entry52.insert(0,data['dictionary'][i]['c3'])
    entry62.delete(0,"end")
    entry62.insert(0,data['dictionary'][i]['c4'])
    entry72.delete(0,"end")
    entry72.insert(0,data['dictionary'][i]['c5'])
    entry82.delete(0,"end")
    entry82.insert(0,data['dictionary'][i]['c6'])
    entry9.delete(0,"end")
    entry9.insert(0,data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])


def copy():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['hangul'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{ "hangul": "X", "hanja": ".", "h1": ".", "c1": ".", "h2": ".", "c2": ".", "h3": ".", "c3": ".", "h4": ".", "c4": ".", "h5": ".", "c5": ".", "h6": ".", "c6": ".", "exp":".", "china":".", "japan":"." }'

        string = string + '\n]}'

        #print(string)

        f = open("data2.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data2.json", "r", encoding = 'utf-8') as f:
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
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    seq = int(entry00.get())

    save_trigger = FALSE

    if(seq>-1 and seq<max):
        save_trigger = TRUE
        data['dictionary'][seq]['hangul'] = entry1.get()
        data['dictionary'][seq]['hanja'] = entry2.get()
        data['dictionary'][seq]['h1'] = entry31.get()
        data['dictionary'][seq]['h2'] = entry41.get()
        data['dictionary'][seq]['h3'] = entry51.get()
        data['dictionary'][seq]['h4'] = entry61.get()
        data['dictionary'][seq]['h5'] = entry71.get()
        data['dictionary'][seq]['h6'] = entry81.get()
        data['dictionary'][seq]['exp'] = entry9.get()
        temp = entry10.get()
        temp = temp.replace("\n", "")
        data['dictionary'][seq]['china'] = temp
        temp = entry11.get()
        temp = temp.replace("\n", "")
        data['dictionary'][seq]['japan'] = temp

        #if(data['dictionary'][seq]['h1'] != "."):
        if(TRUE):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(data['dictionary'][seq]['h1'] == data['dictionary'][j]['hangul'] ):
                    #print(data['dictionary'][j]['hangul'])
                    data['dictionary'][seq]['c1'] = data['dictionary'][j]['hanja']
                    entry32.delete(0,"end")
                    entry32.insert(0,data['dictionary'][seq]['c1'])
                    break

        #if(data['dictionary'][seq]['h2'] != "."):
        if(TRUE):
            for j in range(0, max):
                if(data['dictionary'][seq]['h2'] == data['dictionary'][j]['hangul'] ):
                    data['dictionary'][seq]['c2'] = data['dictionary'][j]['hanja']
                    entry42.delete(0,"end")
                    entry42.insert(0,data['dictionary'][seq]['c2'])
                    break
        
        #if(data['dictionary'][seq]['h3'] != "."):
        if(TRUE):
            for j in range(0, max):
                if(data['dictionary'][seq]['h3'] == data['dictionary'][j]['hangul'] ):
                    data['dictionary'][seq]['c3'] = data['dictionary'][j]['hanja']
                    entry52.delete(0,"end")
                    entry52.insert(0,data['dictionary'][seq]['c3'])
                    break

        #if(data['dictionary'][seq]['h4'] != "."):
        if(TRUE):
            for j in range(0, max):
                if(data['dictionary'][seq]['h4'] == data['dictionary'][j]['hangul'] ):
                    data['dictionary'][seq]['c4'] = data['dictionary'][j]['hanja']
                    entry62.delete(0,"end")
                    entry62.insert(0,data['dictionary'][seq]['c4'])
                    break

        #if(data['dictionary'][seq]['h5'] != "."):
        if(TRUE):
            for j in range(0, max):
                if(data['dictionary'][seq]['h5'] == data['dictionary'][j]['hangul'] ):
                    data['dictionary'][seq]['c5'] = data['dictionary'][j]['hanja']
                    entry72.delete(0,"end")
                    entry72.insert(0,data['dictionary'][seq]['c5'])
                    break
            
        #if(data['dictionary'][seq]['h6'] != "."):
        if(TRUE):
            for j in range(0, max):
                if(data['dictionary'][seq]['h6'] == data['dictionary'][j]['hangul'] ):
                    data['dictionary'][seq]['c6'] = data['dictionary'][j]['hanja']
                    entry82.delete(0,"end")
                    entry82.insert(0,data['dictionary'][seq]['c6'])
                    break

    if(save_trigger == TRUE):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("data2.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()

        entry00.delete(0,"end")
        entry00.insert(0, seq)
        entry01.delete(0,"end")
        entry01.insert(0, "업뎃완료")
        
        



def search_hangul():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry1.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    #entry1.delete(0,"end")
    entry2.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")
    entry32.delete(0,"end")
    entry42.delete(0,"end")
    entry52.delete(0,"end")
    entry62.delete(0,"end")
    entry72.delete(0,"end")
    entry82.delete(0,"end")
    entry9.delete(0,"end")
    entry10.delete(0,"end")
    entry11.delete(0,"end")

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hangul'] == h_temp ):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            entry00.insert(0,result)
            #entry1.insert(0,data['dictionary'][i]['hangul'])
            entry2.insert(0,data['dictionary'][i]['hanja'])
            entry31.insert(0,data['dictionary'][i]['h1'])
            entry41.insert(0,data['dictionary'][i]['h2'])
            entry51.insert(0,data['dictionary'][i]['h3'])
            entry61.insert(0,data['dictionary'][i]['h4'])
            entry71.insert(0,data['dictionary'][i]['h5'])
            entry81.insert(0,data['dictionary'][i]['h6'])
            entry32.insert(0,data['dictionary'][i]['c1'])
            entry42.insert(0,data['dictionary'][i]['c2'])
            entry52.insert(0,data['dictionary'][i]['c3'])
            entry62.insert(0,data['dictionary'][i]['c4'])
            entry72.insert(0,data['dictionary'][i]['c5'])
            entry82.insert(0,data['dictionary'][i]['c6'])
            entry9.insert(0,data['dictionary'][i]['exp'])
            entry10.insert(0,data['dictionary'][i]['china'])
            entry11.insert(0,data['dictionary'][i]['japan'])
            break

    



def search_hanja():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry2.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    #entry2.delete(0,"end")
    entry31.delete(0,"end")
    entry41.delete(0,"end")
    entry51.delete(0,"end")
    entry61.delete(0,"end")
    entry71.delete(0,"end")
    entry81.delete(0,"end")
    entry32.delete(0,"end")
    entry42.delete(0,"end")
    entry52.delete(0,"end")
    entry62.delete(0,"end")
    entry72.delete(0,"end")
    entry82.delete(0,"end")
    entry9.delete(0,"end")
    entry10.delete(0,"end")
    entry11.delete(0,"end")

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hanja'] == h_temp ):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            entry00.insert(0,result)
            entry1.insert(0,data['dictionary'][i]['hangul'])
            #entry2.insert(0,data['dictionary'][i]['hanja'])
            entry31.insert(0,data['dictionary'][i]['h1'])
            entry41.insert(0,data['dictionary'][i]['h2'])
            entry51.insert(0,data['dictionary'][i]['h3'])
            entry61.insert(0,data['dictionary'][i]['h4'])
            entry71.insert(0,data['dictionary'][i]['h5'])
            entry81.insert(0,data['dictionary'][i]['h6'])
            entry32.insert(0,data['dictionary'][i]['c1'])
            entry42.insert(0,data['dictionary'][i]['c2'])
            entry52.insert(0,data['dictionary'][i]['c3'])
            entry62.insert(0,data['dictionary'][i]['c4'])
            entry72.insert(0,data['dictionary'][i]['c5'])
            entry82.insert(0,data['dictionary'][i]['c6'])
            entry9.insert(0,data['dictionary'][i]['exp'])
            entry10.insert(0,data['dictionary'][i]['china'])
            entry11.insert(0,data['dictionary'][i]['japan'])
            break

    
def search_each_hanja():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    seq = int(entry00.get())

    word = list(entry2.get())

    if(len(word)>1):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[0] == data['dictionary'][j]['hanja'] ):
                    entry31.delete(0,"end")
                    entry31.insert(0,data['dictionary'][j]['hangul'])
                    break

    if(len(word)>1):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[1] == data['dictionary'][j]['hanja'] ):
                    entry41.delete(0,"end")
                    entry41.insert(0,data['dictionary'][j]['hangul'])
                    break
        
    if(len(word)>2):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[2] == data['dictionary'][j]['hanja'] ):
                    entry51.delete(0,"end")
                    entry51.insert(0,data['dictionary'][j]['hangul'])
                    break

    if(len(word)>3):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[3] == data['dictionary'][j]['hanja'] ):
                    entry61.delete(0,"end")
                    entry61.insert(0,data['dictionary'][j]['hangul'])
                    break

    if(len(word)>4):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[4] == data['dictionary'][j]['hanja'] ):
                    entry71.delete(0,"end")
                    entry71.insert(0,data['dictionary'][j]['hangul'])
                    break
            
    if(len(word)>5):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[5] == data['dictionary'][j]['hanja'] ):
                    entry81.delete(0,"end")
                    entry81.insert(0,data['dictionary'][j]['hangul'])
                    break

   
    entry01.delete(0,"end")
    entry01.insert(0, "낱자완료")



def next():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    result = int(entry00.get()) + 1

    if(result >= max): 
        result = result - 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['h1'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['h2'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['h3'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['h4'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['h5'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['h6'])
    entry32.delete(0,"end")
    entry32.insert(0,data['dictionary'][i]['c1'])
    entry42.delete(0,"end")
    entry42.insert(0,data['dictionary'][i]['c2'])
    entry52.delete(0,"end")
    entry52.insert(0,data['dictionary'][i]['c3'])
    entry62.delete(0,"end")
    entry62.insert(0,data['dictionary'][i]['c4'])
    entry72.delete(0,"end")
    entry72.insert(0,data['dictionary'][i]['c5'])
    entry82.delete(0,"end")
    entry82.insert(0,data['dictionary'][i]['c6'])
    entry9.delete(0,"end")
    entry9.insert(0,data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])


def previous():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    result = int(entry00.get()) - 1

    if(result < 0): 
        result = result + 1

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['dictionary'][i]['hangul'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['hanja'])
    entry31.delete(0,"end")
    entry31.insert(0,data['dictionary'][i]['h1'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['h2'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['h3'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['h4'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['h5'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['h6'])
    entry32.delete(0,"end")
    entry32.insert(0,data['dictionary'][i]['c1'])
    entry42.delete(0,"end")
    entry42.insert(0,data['dictionary'][i]['c2'])
    entry52.delete(0,"end")
    entry52.insert(0,data['dictionary'][i]['c3'])
    entry62.delete(0,"end")
    entry62.insert(0,data['dictionary'][i]['c4'])
    entry72.delete(0,"end")
    entry72.insert(0,data['dictionary'][i]['c5'])
    entry82.delete(0,"end")
    entry82.insert(0,data['dictionary'][i]['c6'])
    entry9.delete(0,"end")
    entry9.insert(0,data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])


def search_seq():
    with open ("data2.json", "r", encoding = 'utf-8') as f:
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
    entry31.insert(0,data['dictionary'][i]['h1'])
    entry41.delete(0,"end")
    entry41.insert(0,data['dictionary'][i]['h2'])
    entry51.delete(0,"end")
    entry51.insert(0,data['dictionary'][i]['h3'])
    entry61.delete(0,"end")
    entry61.insert(0,data['dictionary'][i]['h4'])
    entry71.delete(0,"end")
    entry71.insert(0,data['dictionary'][i]['h5'])
    entry81.delete(0,"end")
    entry81.insert(0,data['dictionary'][i]['h6'])
    entry32.delete(0,"end")
    entry32.insert(0,data['dictionary'][i]['c1'])
    entry42.delete(0,"end")
    entry42.insert(0,data['dictionary'][i]['c2'])
    entry52.delete(0,"end")
    entry52.insert(0,data['dictionary'][i]['c3'])
    entry62.delete(0,"end")
    entry62.insert(0,data['dictionary'][i]['c4'])
    entry72.delete(0,"end")
    entry72.insert(0,data['dictionary'][i]['c5'])
    entry82.delete(0,"end")
    entry82.insert(0,data['dictionary'][i]['c6'])
    entry9.delete(0,"end")
    entry9.insert(0,data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])

    

label0 = Label(tk,text='SEQ', font=font1).grid(row=0, column=0)
label1 = Label(tk,text='한글', font=font1).grid(row=1, column=0)
label2 = Label(tk,text='한자', font=font1).grid(row=2,column=0)
label3 = Label(tk,text='1', font=font1).grid(row=3,column=0)
label4 = Label(tk,text='2', font=font1).grid(row=4,column=0)
label5 = Label(tk,text='3', font=font1).grid(row=5,column=0)
label6 = Label(tk,text='4', font=font1).grid(row=6,column=0)
label7 = Label(tk,text='5', font=font1).grid(row=7,column=0)
label8 = Label(tk,text='6', font=font1).grid(row=8,column=0)
label9 = Label(tk,text='풀이', font=font1).grid(row=9,column=0)
label10 = Label(tk,text='중국', font=font1).grid(row=10,column=0)
label11 = Label(tk,text='일본', font=font1).grid(row=11,column=0)
label12 = Label(tk,text='영어', font=font1).grid(row=12,column=0)

# 각 단위 입력받는 부분 만들기
entry00 = Entry(tk, width=15, font=font1)
entry01 = Entry(tk, width=10, font=font1)
entry1 = Entry(tk, width=80, font=font1)
entry2 = Entry(tk, width=80, font=font1)

entry31 = Entry(tk, width=80, font=font1)
entry41 = Entry(tk, width=80, font=font1)
entry51 = Entry(tk, width=80, font=font1)
entry61 = Entry(tk, width=80, font=font1)
entry71 = Entry(tk, width=80, font=font1)
entry81 = Entry(tk, width=80, font=font1)

entry32 = Entry(tk, width=10, font=font1)
entry42 = Entry(tk, width=10, font=font1)
entry52 = Entry(tk, width=10, font=font1)
entry62 = Entry(tk, width=10, font=font1)
entry72 = Entry(tk, width=10, font=font1)
entry82 = Entry(tk, width=10, font=font1)

entry9 = Entry(tk, width=80, font=font1)
entry10 = Entry(tk, width=80, font=font1)
entry11 = Entry(tk, width=80, font=font1)

entry00.grid(row=0,column=1)
entry01.grid(row=0,column=2)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

entry31.grid(row=3,column=1)
entry41.grid(row=4,column=1)
entry51.grid(row=5,column=1)
entry61.grid(row=6,column=1)
entry71.grid(row=7,column=1)
entry81.grid(row=8,column=1)

entry32.grid(row=3,column=2)
entry42.grid(row=4,column=2)
entry52.grid(row=5,column=2)
entry62.grid(row=6,column=2)
entry72.grid(row=7,column=2)
entry82.grid(row=8,column=2)

entry9.grid(row=9,column=1)
entry10.grid(row=10,column=1)
entry11.grid(row=11,column=1)


btn5 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq).grid(row=0,column=3)
btn2 = Button(tk,text='한글',bg='black',fg='white',command=search_hangul).grid(row=1,column=2)
btn8 = Button(tk,text='한자',bg='black',fg='white',command=search_hanja).grid(row=2,column=2)

btn1 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=2,column=3)
btn8 = Button(tk,text='낱자',bg='black',fg='white',command=search_each_hanja).grid(row=4,column=3)

btn3 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=6,column=3)
btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=8,column=3)

btn4 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=11,column=2)
btn7 = Button(tk,text='복사',bg='black',fg='white',command=copy).grid(row=11,column=3)

tk.mainloop()









