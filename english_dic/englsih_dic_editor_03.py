import json
from tkinter import *
import tkinter.font


tk = Tk()
tk.geometry("900x140+700+600")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('사전')
tk.wm_attributes("-topmost", 1)


def new():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['english'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{"category": ".", "english": "X", "korean": ".", "example": "."}'

        string = string + '\n]}'

        #print(string)

        f = open("data3.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry01.get()
    result = -1

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['english'] == h_temp ):
            result = i
            break
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    #entry1.delete(0,"end")
    #entry1.insert(0,data['dictionary'][i]['category'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['english'])
    entry3.delete(0,"end")
    entry3.insert(0,data['dictionary'][i]['korean'])
    entry4.delete(0,"end")
    entry4.insert(0,data['dictionary'][i]['example'])



def copy():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)


    #신규데이터추가
    max = len(data['dictionary'])

    if(data['dictionary'][max-1]['english'] != "X"):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string + '{"category": ".", "english": "X", "korean": ".", "example": "."}'

        string = string + '\n]}'

        #print(string)

        f = open("data3.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


    #신규데이터읽기
    entry01.delete(0,"end")
    entry01.insert(0,"X")

    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry01.get()
    result = -1

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['english'] == h_temp ):
            result = i
            break
    
    entry00.delete(0,"end")
    entry00.insert(0,result)


def update_batch():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    save_trigger = TRUE

    for i in range(0,max):
        if data['dictionary'][i]['china'] is not None:
            temp = data['dictionary'][i]['china']
            temp = temp.replace('[', '')
            temp = temp.replace(']', '')
            data['dictionary'][i]['china'] = temp

        #temp_a = temp.split(' ')
        #if(len(temp_a)>1):
        #    data['dictionary'][i]['china'] = temp_a[1] + " " + temp_a[0]
        #else:
        #    data['dictionary'][i]['china'] = temp_a[0]
        

    if(save_trigger == TRUE):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("data3.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()

        entry01.delete(0,"end")
        entry01.insert(0, "Batch완료")



def update():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])

    seq = int(entry00.get())

    save_trigger = FALSE

    if(seq>-1 and seq<max):
        save_trigger = TRUE
        data['dictionary'][seq]['category'] = entry1.get()
        data['dictionary'][seq]['english'] = entry2.get()
        data['dictionary'][seq]['korean'] = entry3.get()
        data['dictionary'][seq]['example'] = entry4.get()

    if(save_trigger == TRUE):
        string =  '{ "dictionary": [\n'

        for i in range(0,max):
            temp = data['dictionary'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)

        f = open("data3.json", 'w', encoding = 'utf-8')
        f.write(string)
        f.close()

        entry00.delete(0,"end")
        entry00.insert(0, seq)
        entry01.delete(0,"end")
        entry01.insert(0, "업뎃완료")
        
        



def search_english():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry2.get()
    result = max - 1


    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    #entry2.delete(0,"end")
    entry3.delete(0,"end")
    entry4.delete(0,"end")


    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['english'] == h_temp ):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry00.delete(0,"end")
            entry00.insert(0,result)
            entry1.insert(0,data['dictionary'][i]['category'])
            #entry2.insert(0,data['dictionary'][i]['english'])
            entry3.insert(0,data['dictionary'][i]['korean'])
            entry4.insert(0,data['dictionary'][i]['example'])
            break

    



def search_korean():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['dictionary'])
    h_temp = entry3.get()
    result = max - 1

    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry00.delete(0,"end")
    entry1.delete(0,"end")
    entry2.delete(0,"end")
    #entry3.delete(0,"end")
    entry4.delete(0,"end")




    stop = 0

    for i in range(0,max):
        if (stop < 1):
            temp = data['dictionary'][i]['korean']
            ref_temp = temp.split(",")
            max2 = len(ref_temp)

            for j in range(0,max2):   
                    if (stop < 1): 
                        if(ref_temp[j] == h_temp ):
                            result = i
                            entry01.delete(0,"end")
                            entry01.insert(0,"조회완료")
                            entry00.delete(0,"end")
                            entry00.insert(0,result)
                            entry1.insert(0,data['dictionary'][i]['category'])
                            entry2.insert(0,data['dictionary'][i]['english'])
                            #entry3.insert(0,data['dictionary'][i]['korean'])
                            entry4.insert(0,data['dictionary'][i]['example'])
                            stop = 1
                            break




def next():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
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
    entry1.insert(0,data['dictionary'][i]['category'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['english'])
    entry3.delete(0,"end")
    entry3.insert(0,data['dictionary'][i]['korean'])
    entry4.delete(0,"end")
    entry4.insert(0,data['dictionary'][i]['example'])


def previous():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
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
    entry1.insert(0,data['dictionary'][i]['category'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['english'])
    entry3.delete(0,"end")
    entry3.insert(0,data['dictionary'][i]['korean'])
    entry4.delete(0,"end")
    entry4.insert(0,data['dictionary'][i]['example'])

def search_seq():
    with open ("data3.json", "r", encoding = 'utf-8') as f:
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
    entry1.insert(0,data['dictionary'][i]['category'])
    entry2.delete(0,"end")
    entry2.insert(0,data['dictionary'][i]['english'])
    entry3.delete(0,"end")
    entry3.insert(0,data['dictionary'][i]['korean'])
    entry4.delete(0,"end")
    entry4.insert(0,data['dictionary'][i]['example'])

    
    

label0 = Label(tk,text='SEQ', font=font1).grid(row=0, column=0)
label4 = Label(tk,text='CAT', font=font1).grid(row=1,column=0)
label1 = Label(tk,text='ENG', font=font1).grid(row=2, column=0)
label2 = Label(tk,text='KOR', font=font1).grid(row=3,column=0)
label3 = Label(tk,text='EX', font=font1).grid(row=4,column=0)


# 각 단위 입력받는 부분 만들기
entry00 = Entry(tk, width=15, font=font1)
entry01 = Entry(tk, width=10, font=font1)
entry1 = Entry(tk, width=80, font=font1)
entry2 = Entry(tk, width=80, font=font1)
entry3 = Entry(tk, width=80, font=font1)
entry4 = Entry(tk, width=80, font=font1)

entry00.grid(row=0,column=1)
entry01.grid(row=0,column=2)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)
entry3.grid(row=3,column=1)
entry4.grid(row=4,column=1)

btn5 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq).grid(row=0,column=3)
btn2 = Button(tk,text='ENG',bg='black',fg='white',command=search_english).grid(row=2,column=2)
btn8 = Button(tk,text='조회',bg='black',fg='white',command=search_korean).grid(row=3,column=2)

btn1 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=2,column=3)

btn3 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=3,column=3)
btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=4,column=3)

btn4 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=4,column=2)


tk.mainloop()









