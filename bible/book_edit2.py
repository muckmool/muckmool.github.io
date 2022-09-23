import json
from tkinter import *
import tkinter.font


tk = Tk()
tk.geometry("920x770+750+200")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('Bible')
tk.wm_attributes("-topmost", 1)


def new():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['book'])
    seq = int(entry00.get())

    if(seq != None):
        string =  '{ "book": [\n'

        for i in range(0,seq+1):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{"bk": ".", "cv": ".", "china": ".", "pinyin": ".", "japan": ".", "hira": ".", "hangul": "."},\n'


        for i in range(seq+1,max):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("bible.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


        #신규데이터읽기
        entry01.delete(0,"end")
        entry01.insert(0,"X")
        entry00.delete(0,"end")
        entry00.insert(0,seq+1)

        with open ("bible.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)
   

        #entry_book.delete(0,"end")
        #entry_book.insert(tkinter.END, data['book'][seq+1]['bk'])
        #entry1.delete(0,"end")
        #entry1.insert(0,data['book'][seq+1]['cv'])
        entry2.delete("1.0", "end-1c")
        entry2.insert(tkinter.END, data['book'][seq+1]['china'])
        entry3.delete("1.0", "end-1c")
        entry3.insert(tkinter.END, data['book'][seq+1]['pinyin'])
        entry4.delete("1.0", "end-1c")
        entry4.insert(tkinter.END, data['book'][seq+1]['japan'])
        entry5.delete("1.0", "end-1c")
        entry5.insert(tkinter.END, data['book'][seq+1]['hira'])
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, data['book'][seq+1]['hangul'])



def delete():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['book'])
    seq = int(entry00.get())

    if(seq != None and seq > -1):
        string =  '{ "book": [\n'

        for i in range(0,seq):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        for i in range(seq+1,max):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("bible.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


        #신규데이터읽기
        entry01.delete(0,"end")
        entry01.insert(0,"X")
        entry00.delete(0,"end")
        entry00.insert(0,seq-1)

        with open ("bible.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)
   

        entry_book.delete(0,"end")
        entry_book.insert(tkinter.END, data['book'][seq-1]['bk'])
        entry1.delete(0,"end")
        entry1.insert(0,data['book'][seq-1]['cv'])
        entry2.delete("1.0", "end-1c")
        entry2.insert(tkinter.END, data['book'][seq-1]['china'])
        entry3.delete("1.0", "end-1c")
        entry3.insert(tkinter.END, data['book'][seq-1]['pinyin'])
        entry4.delete("1.0", "end-1c")
        entry4.insert(tkinter.END, data['book'][seq-1]['japan'])
        entry5.delete("1.0", "end-1c")
        entry5.insert(tkinter.END, data['book'][seq-1]['hira'])
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, data['book'][seq-1]['hangul'])




def update():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])

    seq = int(entry00.get())

    save_trigger = FALSE

    if(seq>-1 and seq<max):
        save_trigger = TRUE
        data['book'][seq]['bk'] = entry_book.get()
        data['book'][seq]['cv'] = entry1.get()
        data['book'][seq]['china'] = entry2.get("1.0", "end-1c")
        data['book'][seq]['pinyin'] = entry3.get("1.0", "end-1c")
        data['book'][seq]['japan'] = entry4.get("1.0", "end-1c")
        data['book'][seq]['hira'] = entry5.get("1.0", "end-1c")
        data['book'][seq]['hangul'] = entry6.get("1.0", "end-1c")


    if(save_trigger == TRUE):
        string =  '{ "book": [\n'

        for i in range(0,max):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("bible.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()

        entry00.delete(0,"end")
        entry00.insert(0, seq)
        entry01.delete(0,"end")
        entry01.insert(0, "업뎃완료")
        
        




def search_seq():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])

    result = max -1

    #print(result)

    if(entry00.get() != ''):
        result = int(entry00.get())

    if(result<0):
        result = 0

    if(result >= max): 
        result = result - 1

    i = result
    
    entry_book.delete(0,"end")
    entry_book.insert(tkinter.END, data['book'][i]['bk'])
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])
    entry2.delete("1.0", "end-1c")
    entry2.insert(tkinter.END, data['book'][i]['china'])
    entry3.delete("1.0", "end-1c")
    entry3.insert(tkinter.END, data['book'][i]['pinyin'])
    entry4.delete("1.0", "end-1c")
    entry4.insert(tkinter.END, data['book'][i]['japan'])
    entry5.delete("1.0", "end-1c")
    entry5.insert(tkinter.END, data['book'][i]['hira'])
    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])


def next():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])
    result = int(entry00.get())

    max = len(data['book'])
    result = int(entry00.get()) + 1

    if(result >= max): 
        result = result - 1

    i = result
    
    entry_book.delete(0,"end")
    entry_book.insert(tkinter.END, data['book'][i]['bk'])
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])
    entry2.delete("1.0", "end-1c")
    entry2.insert(tkinter.END, data['book'][i]['china'])
    entry3.delete("1.0", "end-1c")
    entry3.insert(tkinter.END, data['book'][i]['pinyin'])
    entry4.delete("1.0", "end-1c")
    entry4.insert(tkinter.END, data['book'][i]['japan'])
    entry5.delete("1.0", "end-1c")
    entry5.insert(tkinter.END, data['book'][i]['hira'])
    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])


def previous():
    with open ("bible.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])
    result = int(entry00.get()) - 1

    if(result < 0): 
        result = result + 1

    i = result
    
    entry_book.delete(0,"end")
    entry_book.insert(tkinter.END, data['book'][i]['bk'])
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])
    entry2.delete("1.0", "end-1c")
    entry2.insert(tkinter.END, data['book'][i]['china'])
    entry3.delete("1.0", "end-1c")
    entry3.insert(tkinter.END, data['book'][i]['pinyin'])
    entry4.delete("1.0", "end-1c")
    entry4.insert(tkinter.END, data['book'][i]['japan'])
    entry5.delete("1.0", "end-1c")
    entry5.insert(tkinter.END, data['book'][i]['hira'])
    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])


def trans_china():

    file = open("dic_china.txt", "r", encoding = 'utf-8')     # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
    s = file.read()                                     # 파일에서 문자열 읽기
    #print(s)                                           # Hello, world!
    file.close()                                        # 파일 객체 닫기
    
    s = s.replace("\n", "")
    s = s[:-1]
    read = s.split(',')

    #print(read)



    if(entry2.get("1.0", "end-1c") != None):

        entry3.delete("1.0", "end-1c")

        temp = entry2.get("1.0", "end-1c")

        lst = []
        string = ""

        for i in temp:
            lst.append(i)

        for i in range(0,len(lst)):
            temp2 = lst[i]
            for j in range(0,len(read)):
                if(read[j] == temp2):
                    temp2 = read[j + 1]
                    j = j + 2;
                    break

            string = string + temp2 + " "
        
        entry3.insert(tkinter.END, string)

        #print(lst)



def trans_japan():

    file = open("dic_japan.txt", "r", encoding = 'utf-8')     # hello.txt 파일을 읽기 모드(r)로 열기. 파일 객체 반환
    s = file.read()                                     # 파일에서 문자열 읽기
    #print(s)                                           # Hello, world!
    file.close()                                        # 파일 객체 닫기
    
    s = s.replace("\n", "")
    s = s[:-1]
    read = s.split(',')

    #print(read)



    if(entry4.get("1.0", "end-1c") != None):

        entry5.delete("1.0", "end-1c")

        temp = entry4.get("1.0", "end-1c")

        lst = []
        string = ""

        for i in temp:
            lst.append(i)

        for i in range(0,len(lst)):
            temp2 = lst[i]
            for j in range(0,len(read)):
                if(read[j] == temp2):
                    temp2 = read[j + 1]
                    j = j + 2;
                    break

            string = string + temp2
        
        entry5.insert(tkinter.END, string)

        #print(lst)



label0 = Label(tk,text='BOOK', font=font1).grid(row=0, column=0)
label1 = Label(tk,text='장절', font=font1).grid(row=1, column=0)
label2 = Label(tk,text='SEQ',  font=font1).grid(row=2, column=0)
label3 = Label(tk,text='중국', font=font1).grid(row=3, column=0)
label4 = Label(tk,text='병음', font=font1).grid(row=4, column=0)
label5 = Label(tk,text='일본', font=font1).grid(row=5, column=0)
label6 = Label(tk,text='발음', font=font1).grid(row=6, column=0)
label7 = Label(tk,text='한글', font=font1).grid(row=7, column=0)


# 각 단위 입력받는 부분 만들기
entry_book = Entry(tk, width=15, font=font1)
entry01 = Entry(tk, width=10, font=font1)
entry1 = Entry(tk, width=15, font=font1)
entry00 = Entry(tk, width=15, font=font1)

entry2 = Text(tk, width=80, height =7, font=font1)
entry3 = Text(tk, width=80, height =7, font=font1)
entry4 = Text(tk, width=80, height =7, font=font1)
entry5 = Text(tk, width=80, height =7, font=font1)
entry6 = Text(tk, width=80, height =7, font=font1)


entry_book.grid(row=0,column=1)
entry01.grid(row=0,column=2)
entry1.grid(row=1,column=1)
entry00.grid(row=2,column=1)

entry2.grid(row=3,column=1)
entry3.grid(row=4,column=1)
entry4.grid(row=5,column=1)
entry5.grid(row=6,column=1)
entry6.grid(row=7,column=1)


btn8 = Button(tk,text='장절조회',bg='black',fg='white',command=search_seq).grid(row=0,column=3)
btn1 = Button(tk,text='seq조회',bg='black',fg='white',command=search_seq).grid(row=2,column=3)

btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=3,column=2)
btn7 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=3,column=3)

btn4 = Button(tk,text='중국병음',bg='black',fg='white',command=trans_china).grid(row=4,column=2)
btn5 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=5,column=3)
btn4 = Button(tk,text='일본발음',bg='black',fg='white',command=trans_japan).grid(row=6,column=2)

btn2 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=7,column=3)
btn3 = Button(tk,text='삭제',bg='black',fg='white',command=delete).grid(row=7,column=2)




tk.mainloop()

