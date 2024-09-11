import json
from tkinter import *
import tkinter.font
import time
import atexit


#Global 변수----------------------------------

global count_sum
count_sum = 10


#GUI 정의-------------------------------------------------

tk = Tk()
tk.geometry("850x350-3+3")
font8 = tkinter.font.Font(family="Consolas", size=8)
font4 = tkinter.font.Font(family="Consolas", size=11)
font5 = tkinter.font.Font(family="Consolas", size=24)
font1 = tkinter.font.Font(family="Consolas", size=12)
font6 = tkinter.font.Font(family="Consolas", size=13)
font2 = tkinter.font.Font(family="Consolas", size=14)
font3 = tkinter.font.Font(family="Consolas", size=15)
font7 = tkinter.font.Font(family="Consolas", size=16)
tk.title('개역개정 4')
tk.wm_attributes("-topmost", 0)



#성경 편집 함수들 -------------------------------------------------


def new():

    update()

    book_name = book_name_search()
    with open (book_name, "r", encoding = 'utf-8') as f:
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

        string = string + '{"cv": ".", "hangul": "."},\n'


        for i in range(seq+1,max):
            temp = data['book'][i]
            temp = json.dumps(temp, ensure_ascii=False)
            string = string + temp + ',\n'

        string = string[:-2]

        string = string + '\n]}'

        #print(string)
        book_name = book_name_search()
        f = open(book_name, 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


        #신규데이터읽기
        entry01.delete(0,"end")
        entry01.insert(0,"X")
        entry00.delete(0,"end")
        entry00.insert(0,seq+1)

        book_name = book_name_search()
        with open (book_name, "r", encoding = 'utf-8') as f:
            data = json.load(f)


        temp = entry1.get()
        if(temp is not NONE):
            temp = temp.split(':')
            temp2 = str( int(temp[1]) + 1)
            temp3 = temp[0] + ":" + temp2
            entry1.delete(0,"end")
            entry1.insert(0,temp3)
   


        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, data['book'][seq+1]['hangul'])


        



def delete():
    book_name = book_name_search()
    with open (book_name, "r", encoding = 'utf-8') as f:
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
        book_name = book_name_search()
        f = open(book_name, 'w', encoding = 'utf-8')
        f.write(string)
        f.close()


        #신규데이터읽기
        entry01.delete(0,"end")
        entry01.insert(0,"X")
        entry00.delete(0,"end")
        entry00.insert(0,seq-1)

        book_name = book_name_search()
        with open (book_name, "r", encoding = 'utf-8') as f:
            data = json.load(f)
   

        
        entry1.delete(0,"end")
        entry1.insert(0,data['book'][seq-1]['cv'])

        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, data['book'][seq-1]['hangul'])




def update():
    book_name = book_name_search()
    with open (book_name, "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])

    seq = int(entry00.get())

    save_trigger = FALSE

    if(seq>-1 and seq<max):
        save_trigger = TRUE
     
        data['book'][seq]['cv'] = entry1.get()

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
        book_name = book_name_search()
        f = open(book_name, 'w', encoding = 'utf-8')
        f.write(string)
        f.close()



        entry00.delete(0,"end")
        entry00.insert(0, seq)
        entry01.delete(0,"end")
        entry01.insert(0, "업뎃" + str(count_sum))



        
        
def search_cv():
    book_name = book_name_search()
    #print(book_name)

    with open (book_name, "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])

    result = max -1

    #print(result)

    if(entry1.get() != ''):
        result = entry1.get()

    for i in range(0,max):
        if(data['book'][i]['cv'] == result):
            result = i
            break

    i = result
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")
    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])

    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])




def search_seq():
    book_name = book_name_search()
    #print(book_name)

    with open (book_name, "r", encoding = 'utf-8') as f:
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
    
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")

    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])

    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])



def next():
    book_name = book_name_search()
    with open (book_name, "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])
    result = int(entry00.get())

    max = len(data['book'])
    result = int(entry00.get()) + 1

    if(result >= max): 
        result = result - 1

    i = result
    
     
     
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")

    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])

    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])



def previous():
    book_name = book_name_search()
    with open (book_name, "r", encoding = 'utf-8') as f:
        data = json.load(f)

    max = len(data['book'])
    result = int(entry00.get()) - 1

    if(result < 0): 
        result = result + 1

    i = result
    
     
     
    entry00.delete(0,"end")
    entry00.insert(0,result)
    entry01.delete(0,"end")

    entry1.delete(0,"end")
    entry1.insert(0,data['book'][i]['cv'])

    entry6.delete("1.0", "end-1c")
    entry6.insert(tkinter.END, data['book'][i]['hangul'])



def change_book():
    book_name = [    
                    "창세기  Genesis",
                    "출애굽기  Exodus",
                    "레위기  Leviticus",
                    "민수기  Numbers",
                    "신명기  Dueterronomy",
                    "여호수아서  Joshua",
                    "사사기  Judges",
                    "룻기  Ruth",
                    "사무엘상  1 Samuel",
                    "사무엘하  2 Samuel",
                    "열왕기상  1 Kings",
                    "열왕기하  2 Kings",
                    "역대기상  1 Chronicles",
                    "역대기하  2 Chronicles",
                    "에스라서  Ezra",
                    "느헤미야서  Nehemiah",
                    "에스더서  Esther",
                    "욥기  Job",
                    "시편  Psalms",
                    "잠언  Proverbs",
                    "전도서  Ecclesiastes",
                    "아가  Song of Solomon",
                    "이사야서  Isaiah",
                    "예레미야서  Jeremiah",
                    "예레미야애가  Lamentations",
                    "에스겔서  Ezekiel",
                    "다니엘서  Daniel",
                    "호세아서  Hosea",
                    "요엘서  Joel",
                    "아모스서  Amos",
                    "오바댜서  Obadiah",
                    "요나서  Jonah",
                    "미가  Micah",
                    "나훔  Nahum",
                    "하박국  Habakkuk",
                    "스바냐  Zephaniah",
                    "학개  Haggai",
                    "스가랴  Zechariah",
                    "말라기  Malachi",
                    "마태복음  Matthew",
                    "마가복음  Mark",
                    "누가복음  Luke",
                    "요한복음  John",
                    "사도행전  Acts",
                    "로마서  Romans",
                    "고린도전서  1 Corinthians",
                    "고린도후서  2 Corinthians",
                    "갈라디아서  Galatians",
                    "에베소서  Ephesians",
                    "빌립보서  Philippians",
                    "골로새서  Colossians",
                    "데살로니가전서  1 Thessalonians",
                    "데살로니가후서  2 Thessalonians",
                    "디모데전서  1 Timothy",
                    "디모데후서  2 Timothy",
                    "디도서  Titus",
                    "빌레몬서  Philemon",
                    "히브리서  Hebrews",
                    "야고보서  James",
                    "베드로전서  1 Peter",
                    "베드로후서  2 Peter",
                    "요한1서  1 John",
                    "요한2서  2 John",
                    "요한3서  3 John",
                    "유다서  Jude",
                    "요한계시록  Revelation"
                ]

    if(entry_book_no.get() != ''):
        result = int(entry_book_no.get())
        if(result<1): 
            result = 1
        if(result>66):
            result = 66
        entry_book.delete(0,"end")
        entry_book.insert(tkinter.END, book_name[result-1])
        entry_book_no.delete(0,"end")
        entry_book_no.insert(tkinter.END, result)
        entry00.delete(0,"end")
        entry00.insert(tkinter.END, "0")
        search_seq()
        



def book_name_search():
    book_list = [
                    "book/book_01.json",
                    "book/book_02.json",
                    "book/book_03.json",
                    "book/book_04.json",
                    "book/book_05.json",
                    "book/book_06.json",
                    "book/book_07.json",
                    "book/book_08.json",
                    "book/book_09.json",
                    "book/book_10.json",
                    
                    "book/book_11.json",
                    "book/book_12.json",
                    "book/book_13.json",
                    "book/book_14.json",
                    "book/book_15.json",
                    "book/book_16.json",
                    "book/book_17.json",
                    "book/book_18.json",
                    "book/book_19.json",
                    "book/book_20.json",

                    "book/book_21.json",
                    "book/book_22.json",
                    "book/book_23.json",
                    "book/book_24.json",
                    "book/book_25.json",
                    "book/book_26.json",
                    "book/book_27.json",
                    "book/book_28.json",
                    "book/book_29.json",
                    "book/book_30.json",

                    "book/book_31.json",
                    "book/book_32.json",
                    "book/book_33.json",
                    "book/book_34.json",
                    "book/book_35.json",
                    "book/book_36.json",
                    "book/book_37.json",
                    "book/book_38.json",
                    "book/book_39.json",
                    "book/book_40.json",

                    "book/book_41.json",
                    "book/book_42.json",
                    "book/book_43.json",
                    "book/book_44.json",
                    "book/book_45.json",
                    "book/book_46.json",
                    "book/book_47.json",
                    "book/book_48.json",
                    "book/book_49.json",
                    "book/book_50.json",

                    "book/book_51.json",
                    "book/book_52.json",
                    "book/book_53.json",
                    "book/book_54.json",
                    "book/book_55.json",
                    "book/book_56.json",
                    "book/book_57.json",
                    "book/book_58.json",
                    "book/book_59.json",
                    "book/book_60.json",

                    "book/book_61.json",
                    "book/book_62.json",
                    "book/book_63.json",
                    "book/book_64.json",
                    "book/book_65.json",
                    "book/book_66.json"
                ]

    result = 1

    if(entry_book_no.get() != ''):
        result = int(entry_book_no.get())
        if(result<1): 
            result = 1
        if(result>2):
            result = 2

    return book_list[result-1]




#GUI 구성 요소들---------------------------------------------------

label0 = Label(tk,text='B_NO',  font=font1).grid(row=0, column=0)

label1 = Label(tk,text='BOOK', font=font1).grid(row=1, column=0)

label2 = Label(tk,text='SEQ',  font=font1).grid(row=2, column=0)

label3 = Label(tk,text='장절', font=font1).grid(row=3, column=0)

label7 = Label(tk,text='한글', font=font1).grid(row=4, column=0)




# 각 단위 입력받는 부분 만들기
entry_book_no = Entry(tk, width=50, font=font2)  # book no
entry_book_no.grid(row=0,column=1)     

entry_book = Entry(tk, width=50, font=font2) # book name
entry_book.grid(row=1,column=1)     

entry00 = Entry(tk, width=50, font=font2)    # SEQ
entry00.grid(row=2,column=1)        

entry1 = Entry(tk, width=50, font=font2)     # 장절
entry1.grid(row=3,column=1)         

entry01 = Entry(tk, width=8, font=font2)     # 결과
entry01.grid(row=1, column=2)       # 결과

entry6 = Text(tk, width=70, height =8, font=font2) # 한글 내용
entry6.grid(row=5,column=1)         # 한글 내용


# 각 단위 입력받는 부분 기본 값

entry_book_no.delete(0,"end")
entry_book_no.insert(tkinter.END, "1")
entry_book.delete(0,"end")
entry_book.insert(tkinter.END, "창세기")

# 버튼 정의 및 배치

btn0 = Button(tk,text='책 변경',bg='black',fg='white', font=font8, command=change_book).grid(row=0,column=2)

btn1 = Button(tk,text='seq 조회',bg='black',fg='white', font=font8, command=search_seq).grid(row=2,column=2)
btn8 = Button(tk,text='장절 조회',bg='black',fg='white', font=font8, command=search_cv).grid(row=3,column=2)


btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=4,column=2)
btn7 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=5,column=2)



btn3 = Button(tk,text='삭제',bg='orange',fg='white',  font=font8, command=delete).grid(row=6, column=0)
btn5 = Button(tk,text='수정',bg='blue',fg='white',command=update).grid(row=6,column=1)
btn2 = Button(tk,text='신규',bg='green',fg='white',command=new).grid(row=6,column=2)




def quit():
    
    tk.quit()


tk.mainloop()

