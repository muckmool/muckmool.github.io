import json
from tkinter import *
import tkinter.font
import time
import atexit


#Global 변수----------------------------------

global count_sum
count_sum = 30


#GUI 정의-------------------------------------------------

tk = Tk()
tk.geometry("930x740-3+100")
font8 = tkinter.font.Font(family="Consolas", size=8)
font4 = tkinter.font.Font(family="Consolas", size=11)
font5 = tkinter.font.Font(family="Consolas", size=24)
font1 = tkinter.font.Font(family="Consolas", size=12)
font6 = tkinter.font.Font(family="Consolas", size=13)
font2 = tkinter.font.Font(family="Consolas", size=14)
font3 = tkinter.font.Font(family="Consolas", size=15)
font7 = tkinter.font.Font(family="Consolas", size=16)
tk.title('윤동주')
tk.wm_attributes("-topmost", 1)



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

        string = string + '{"cv": ".", "china": ".", "pinyin": ".", "japan": ".", "hira": ".", "hangul": ".", "english": ".", "exp": "."},\n'


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
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, data['book'][seq+1]['english'])
        entry13.delete("1.0", "end-1c")
        entry13.insert(tkinter.END, data['book'][seq+1]['exp'])

        #write_d()


        



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
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, data['book'][seq-1]['english'])
        entry13.delete("1.0", "end-1c")
        entry13.insert(tkinter.END, data['book'][seq-1]['exp'])



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
        data['book'][seq]['china'] = entry2.get("1.0", "end-1c")
        data['book'][seq]['pinyin'] = entry3.get("1.0", "end-1c")
        data['book'][seq]['japan'] = entry4.get("1.0", "end-1c")
        data['book'][seq]['hira'] = entry5.get("1.0", "end-1c")
        data['book'][seq]['hangul'] = entry6.get("1.0", "end-1c")
        data['book'][seq]['english'] = entry7.get("1.0", "end-1c")
        data['book'][seq]['exp'] = entry13.get("1.0", "end-1c")


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


        global count_sum


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
    entry7.delete("1.0", "end-1c")
    entry7.insert(tkinter.END, data['book'][i]['english'])
    entry13.delete("1.0", "end-1c")
    entry13.insert(tkinter.END, data['book'][i]['exp'])



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
    entry7.delete("1.0", "end-1c")
    entry7.insert(tkinter.END, data['book'][i]['english'])
    entry13.delete("1.0", "end-1c")
    entry13.insert(tkinter.END, data['book'][i]['exp'])


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
    entry7.delete("1.0", "end-1c")
    entry7.insert(tkinter.END, data['book'][i]['english'])
    entry13.delete("1.0", "end-1c")
    entry13.insert(tkinter.END, data['book'][i]['exp'])


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
    entry7.delete("1.0", "end-1c")
    entry7.insert(tkinter.END, data['book'][i]['english'])
    entry13.delete("1.0", "end-1c")
    entry13.insert(tkinter.END, data['book'][i]['exp'])



def trans_china():

    #with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)

    data = g_data

    max = len(data['dictionary'])


    if(entry2.get("1.0", "end-1c") != None):

        entry3.delete("1.0", "end-1c")

        temp = entry2.get("1.0", "end-1c")

        lst = []
        string = ""

        for i in temp:
            lst.append(i)

        for i in range(0,len(lst)):
            temp2 = lst[i]
            for j in range(0,max):
                if(data['dictionary'][j]['hanja'] == temp2):
                    temp2 = data['dictionary'][j]['china']                     
                    break

            string = string + temp2 + "_"
        
        entry3.insert(tkinter.END, string)

        #print(lst)

    update()






def trans_japan():

    #with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)

    data = g_data

    max = len(data['dictionary'])


    if(entry4.get("1.0", "end-1c") != None):

        temp = entry4.get("1.0", "end-1c")

        # 특수 문자 삭제
        temp = temp.replace('．',' . ')
        temp = temp.replace('，',' , ')
        temp = temp.replace('?',' ? ')
        temp = temp.replace('「','')
        temp = temp.replace('」','')
        temp = temp.replace('¿','々')
        temp = temp.replace('、',' 、 ')
        temp = temp.replace('。',' 。 ')
        temp = temp.replace('\n',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')



        entry4.delete("1.0", "end-1c")
        entry4.insert(tkinter.END, temp)


        entry5.delete("1.0", "end-1c")

        temp = entry4.get("1.0", "end-1c")

        lst = []
        string = ""

        temp = temp.split(" ")

        for i in range(0,len(temp)):
            temp2 = temp[i]
            for j in range(0,max):
                if(data['dictionary'][j]['hanja'] == temp2):
                    temp2 = data['dictionary'][j]['japan']                     
                    break
            string = string + temp2 + "_"
        
        entry5.insert(tkinter.END, string)





    if(entry6.get("1.0", "end-1c") != None):

        temp = entry6.get("1.0", "end-1c")

        # 특수 문자 삭제
        temp = temp.replace('\n',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')  

        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)

    if(entry7.get("1.0", "end-1c") != None):

        temp = entry7.get("1.0", "end-1c")

        # 특수 문자 삭제
        temp = temp.replace('\n',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')
        temp = temp.replace('  ',' ')   

        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)


    #등장 인물

    if(entry4.get("1.0", "end-1c") == 'お婆ちゃん'):
        temp = '할머니'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '三葉'):
        temp = '미츠하'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '四葉'):
        temp = '요츠하'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '早耶香'):
        temp = '사야까'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '克彦'):
        temp = '카츠히코'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '瀧'):
        temp = '타키'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '瀧の父'):
        temp = '타키 아버지'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, "타키노 치치")

    if(entry4.get("1.0", "end-1c") == '同級生'):
        temp = '동급생'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, "도우큐쎄이")

    if(entry4.get("1.0", "end-1c") == 'ツカサ'):
        temp = '츠카사'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)

    if(entry4.get("1.0", "end-1c") == '慎太'):
        temp = '신타'
        entry6.delete("1.0", "end-1c")
        entry6.insert(tkinter.END, temp)
        entry7.delete("1.0", "end-1c")
        entry7.insert(tkinter.END, temp)



    update()



def trans_korea():

    #with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)

    data = g_data

    max = len(data['dictionary'])

    input_temp = entry4.get("1.0", "end-1c") 

    if(input_temp != None):

        entry13.delete("1.0", "end-1c")

        temp = entry4.get("1.0", "end-1c")

        lst = []
        string = ""

        for i in temp:
            lst.append(i)

        for i in range(0,len(lst)):
            temp2 = lst[i]
            for j in range(0,max):
                if(temp2 != "."):
                    if(data['dictionary'][j]['hanja'] == temp2):
                        string = string + temp2 + " " + data['dictionary'][j]['hangul'] + " "            
                        break


        string = string.strip(".")
        
        entry13.insert(tkinter.END, string)

        #print(lst)

    update()






def search_book():
    book_name = [   "없음", 
                    "창세기  Genesis  创世纪  創世記",
                    "출애굽기  Exodus  出埃及记  出エジプト記",
                    "레위기  Leviticus  利未记  レビ記",
                    "민수기  Numbers  民数记  民數記",
                    "신명기  Dueterronomy  申命记  申命記",
                    "여호수아서  Joshua  约书亚记  ヨシュア記",
                    "사사기  Judges  士师记  士師記",
                    "룻기  Ruth  路得记  ルツ記",
                    "사무엘상  1 Samuel  撒母耳记上  サムエル記上",
                    "사무엘하  2 Samuel  撒母耳记下  サムエル記下",
                    "열왕기상  1 Kings  列王纪上  列王紀上",
                    "열왕기하  2 Kings  列王纪下  列王紀下",
                    "역대기상  1 Chronicles  历代志上  歷代志上",
                    "역대기하  2 Chronicles  历代志下  歷代志下",
                    "에스라서  Ezra  以斯拉记  エズラ記",
                    "느헤미야서  Nehemiah  尼希米记  ネヘミヤ記",
                    "에스더서  Esther  以斯帖记  エステル記",
                    "욥기  Job  约伯记  ヨブ記",
                    "시편  Psalms  诗篇  詩篇",
                    "잠언  Proverbs  箴言  箴言",
                    "전도서  Ecclesiastes  传道书  傳道の書",
                    "아가  Song of Solomon  雅歌  雅歌",
                    "이사야서  Isaiah  以赛亚书  イザヤ書",
                    "예레미야서  Jeremiah  耶利米书  エレミヤ書",
                    "예레미야애가  Lamentations  耶利米哀歌  哀歌",
                    "에스겔서  Ezekiel  以西结书  エゼキエル書",
                    "다니엘서  Daniel  但以理书  ダニエル書",
                    "호세아서  Hosea  何西阿书  ホセア書",
                    "요엘서  Joel  约珥书  ヨエル書",
                    "아모스서  Amos  阿摩司书  アモス書",
                    "오바댜서  Obadiah  俄巴底亚书  オバデヤ書",
                    "요나서  Jonah  约拿书  ヨナ書",
                    "미가  Micah  弥迦书  ミカ書",
                    "나훔  Nahum  那鸿书  ナホム書",
                    "하박국  Habakkuk  哈巴谷书  ハバクク書",
                    "스바냐  Zephaniah  西番雅书  ゼパニヤ書",
                    "학개  Haggai  哈该书  ハガイ書",
                    "스가랴  Zechariah  撒迦利亚书  ゼカリヤ書",
                    "말라기  Malachi  玛拉基书  マラキ書",
                    "마태복음  Matthew  马太福音  マタイによる福音書",
                    "마가복음  Mark  马可福音  マルコによる福音書",
                    "누가복음  Luke  路加福音  ルカによる福音書",
                    "요한복음  John  约翰福音  ヨハネによる福音書",
                    "사도행전  Acts  使徒行传  使徒行傳",
                    "로마서  Romans  罗马书  ロ―マ人への手紙",
                    "고린도전서  1 Corinthians  歌林多前书  コリント人への第一の手紙",
                    "고린도후서  2 Corinthians  歌林多后书  コリント人への第二の手紙",
                    "갈라디아서  Galatians  加拉太书  ガラテヤ人への手紙",
                    "에베소서  Ephesians  以弗所书  エペソ人への手紙",
                    "빌립보서  Philippians  腓利比书  ピリピ人への手紙",
                    "골로새서  Colossians  歌罗西书  コロサイ人への手紙",
                    "데살로니가전서  1 Thessalonians  帖撒罗尼迦前书  テサロニケ人への第一の手紙",
                    "데살로니가후서  2 Thessalonians  帖撒罗尼迦后书  テサロニケ人への第二の手紙",
                    "디모데전서  1 Timothy  提摩太前书  テモテへの第一の手紙",
                    "디모데후서  2 Timothy  提摩太后书  テモテへの第二の手紙",
                    "디도서  Titus  提多书  テトスへの手紙",
                    "빌레몬서  Philemon  腓利门书  ピレモンへの手紙",
                    "히브리서  Hebrews  希伯来书  ヘブル人への手紙",
                    "야고보서  James  雅各书  ヤコブの手紙",
                    "베드로전서  1 Peter  彼得前书  ペテロの第一の手紙",
                    "베드로후서  2 Peter  彼得后书  ペテロの第二の手紙",
                    "요한1서  1 John  约翰一书  ヨハネの第一の手紙",
                    "요한2서  2 John  约翰二书  ヨハネの第二の手紙",
                    "요한3서  3 John  约翰三书  ヨハネの第三の手紙",
                    "유다서  Jude  犹大书  ユダの手紙",
                    "요한계시록  Revelation  启示录  ヨハネの默示錄"
                ]

    if(entry_book_no.get() != ''):
        result = int(entry_book_no.get())
        if(result<1): 
            result = 1
        if(result>66):
            result = 66
        entry_book.delete(0,"end")
        entry_book.insert(tkinter.END, book_name[result])
        entry_book_no.delete(0,"end")
        entry_book_no.insert(tkinter.END, result)


def book_name_search():
    book_list = [
                    "bible_data/01_genesis.json",
                    "bible_data/02_exodus.json",
                    "03_leviticus.json",
                    "04_numbers.json",
                    "05_dueterronomy.json",
                    "06_joshua.json",
                    "07_judges.json",
                    "08_ruth.json",
                    "09_samuel_1.json",
                    "10_samuel_2.json",
                    "11_kings_1.json",
                    "12_kings_2.json",
                    "13_chronicles_1.json",
                    "14_chronicles_2.json",
                    "15_ezra.json",
                    "16_nehemiah.json",
                    "17_esther.json",
                    "18_job.json",
                    "19_psalms.json",
                    "20_proverbs.json",
                    "21_ecclesiastes.json",
                    "22_songofsolomon.json",
                    "23_isaiah.json",
                    "24_jeremiah.json",
                    "25_lamentations.json",
                    "26_ezekiel.json",
                    "27_daniel.json",
                    "28_hosea.json",
                    "29_joel.json",
                    "30_amos.json",
                    "31_obadiah.json",
                    "32_jonah.json",
                    "33_micah.json",
                    "34_nahum.json",
                    "35_habakkuk.json",
                    "36_zephaniah.json",
                    "37_haggai.json",
                    "38_zechariah.json",
                    "39_malachi.json",
                    "40_matthew.json",
                    "41_mark.json",
                    "bible_data/42_luke.json",
                    "43_john.json",
                    "44_acts.json",
                    "45_romans.json",
                    "46_corinthians_1.json",
                    "47_corinthians_2.json",
                    "48_galatians.json",
                    "49_ephesians.json",
                    "50_philippians.json",
                    "51_colossians.json",
                    "52_thessalonians_1.json",
                    "53_thessalonians_2.json",
                    "54_timothy_1.json",
                    "55_timothy_2.json",
                    "56_titus.json",
                    "57_philemon.json",
                    "58_hebrews.json",
                    "59_james.json",
                    "60_peter_1.json",
                    "61_peter_2.json",
                    "62_john_1.json",
                    "63_john_2.json",
                    "64_john_3.json",
                    "65_jude.json",
                    "66_revelation.json",
                    "japan_book_data/73_yoondongju.json"

           ]

    result = 67

    if(entry_book_no.get() != ''):
        result = int(entry_book_no.get())
        if(result<1): 
            result = 1
        if(result>67):
            result = 67

    return book_list[result-1]


#dictionary 함수들-------------------------------------------------


def new_d():

    new_string = '{ "hangul": "X", "hanja": ".", "h1": ".", "c1": ".", "h2": ".", "c2": ".", "h3": ".", "c3": ".", "h4": ".", "c4": ".", "h5": ".", "c5": ".", "h6": ".", "c6": ".", "exp":".", "china":".", "japan":"." , "english":"." }'

    add_json = json.loads(new_string)

    g_data['dictionary'].append(add_json)

    entry9.delete(0,"end")

    search_seq_d()

    entry01.delete(0,"end")
    entry01.insert(0,"신규완료")


def delete_d():

    if(entry9.get() != ''):
        target = int(entry9.get())

    g_data['dictionary'].pop(target)

    
    target = target - 1
    
    entry9.delete(0,target)

    search_seq_d()

    entry01.delete(0,"end")
    entry01.insert(0,"삭제완료")



def update_d():

    max = len(g_data['dictionary'])

    seq = int(entry9.get())
    g_data['dictionary'][seq]['hanja'] = entry10.get()

    temp = entry11.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['japan'] = temp

    temp = entry12.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['china'] = temp

    temp = entry14.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['hangul'] = temp

    search_seq_d()
    
    entry01.delete(0,"end")
    entry01.insert(0, "업뎃완료")

    global count_sum
    count_sum = count_sum - 1
    #print(count_sum) 

    if(count_sum < 1): 
        count_sum = count_sum + 30
        write_d()


def search_seq_d():
    #with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)

    data = g_data
    
    max = len(data['dictionary']) - 1

    result = max

    if(entry9.get() != ''):
        result = int(entry9.get())

    if(result<0):
        result = 0

    if(result > max): 
        result = max - 1

    i = result
    
    entry9.delete(0,"end")
    entry9.insert(0,result)
    entry01.delete(0,"end")
    entry01.insert(0,"조회완료")
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['hanja'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])
    entry12.delete(0,"end")
    entry12.insert(0,data['dictionary'][i]['china'])
    entry14.delete(0,"end")
    entry14.insert(0,data['dictionary'][i]['hangul'])


def search_hanja_d():
    #with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

    max = len(data['dictionary'])
    h_temp = entry10.get()
    result = max - 1

    entry01.delete(0,"end")
    entry01.insert(0,"없음")
    entry9.delete(0,"end")
    entry10.delete(0,"end")
    entry11.delete(0,"end")
    entry12.delete(0,"end")
    entry14.delete(0,"end")

    for i in range(0,max):
        #print(data['dictionary'][i]['hangul'])
        if(data['dictionary'][i]['hanja'] == h_temp ):
            result = i
            entry01.delete(0,"end")
            entry01.insert(0,"조회완료")
            entry9.delete(0,"end")
            entry9.insert(0,result)
            entry10.insert(0,data['dictionary'][i]['hanja'])
            entry11.insert(0,data['dictionary'][i]['japan'])
            entry12.insert(0,data['dictionary'][i]['china'])
            entry14.insert(0,data['dictionary'][i]['hangul'])
            break



def read_d():
    with open ("dic/data3.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    global g_data
    
    g_data = data

    #print(g_data['dictionary'][3])
    
    entry01.delete(0,"end")
    entry01.insert(0, "읽기완료")


def write_d():

    #update_d()

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

    f = open("dic/data3.json", 'w', encoding = 'utf-8')
    f.write(string)
    f.close()

    #entry00.delete(0,"end")
    #entry00.insert(0, seq)
    entry01.delete(0,"end")
    entry01.insert(0, "저장완료")



#GUI 구성 요소들---------------------------------------------------


label0 = Label(tk,text='BOOK', font=font1).grid(row=0, column=0)
label1 = Label(tk,text='장절', font=font1).grid(row=1, column=0)
label2 = Label(tk,text='SEQ',  font=font1).grid(row=2, column=0)
label3 = Label(tk,text='중X', font=font1).grid(row=3, column=0)
label4 = Label(tk,text='병X', font=font1).grid(row=4, column=0)
label5 = Label(tk,text='일본', font=font1).grid(row=5, column=0)
label6 = Label(tk,text='히라', font=font1).grid(row=6, column=0)
label7 = Label(tk,text='발음', font=font1).grid(row=7, column=0)
label13 = Label(tk,text='뜻음', font=font1).grid(row=8, column=0)
label8 = Label(tk,text='한글', font=font1).grid(row=9, column=0)

label9 = Label(tk,text='SEQ', font=font1).grid(row=10, column=0)
label10 = Label(tk,text='한자', font=font1).grid(row=11, column=0)
label14 = Label(tk,text='한국', font=font1).grid(row=12, column=0)
label11 = Label(tk,text='일본', font=font1).grid(row=13, column=0)
label12 = Label(tk,text='중국', font=font1).grid(row=14, column=0)


# 각 단위 입력받는 부분 만들기
entry_book_no = Entry(tk, width=5, font=font1)
entry_book = Entry(tk, width=80, font=font1)
entry01 = Entry(tk, width=8, font=font8)
entry1 = Entry(tk, width=30, font=font1)
entry00 = Entry(tk, width=30, font=font1)

entry2 = Text(tk, width=46, height =1, font=font5)
entry3 = Text(tk, width=92, height =1, font=font6)
entry4 = Text(tk, width=69, height =5, font=font7)
entry5 = Text(tk, width=83, height =4, font=font2)
entry7 = Text(tk, width=83, height =4, font=font2)
entry13 = Text(tk, width=83, height =2, font=font2)
entry6 = Text(tk, width=83, height =4, font=font2)

entry9 = Entry(tk, width=88, font=font1)
entry10 = Entry(tk, width=66, font=font7)
entry14 = Entry(tk, width=66, font=font7)
entry11 = Entry(tk, width=66, font=font7)
entry12 = Entry(tk, width=66, font=font7)


entry_book.grid(row=0,column=1)
entry01.grid(row=0, column=2)
#entry_book_no.grid(row=0,column=2)

entry1.grid(row=1,column=1)

entry00.grid(row=2,column=1)

entry2.grid(row=3,column=1)
entry3.grid(row=4,column=1)
entry4.grid(row=5,column=1)
entry5.grid(row=6,column=1)
entry7.grid(row=7,column=1)
entry13.grid(row=8,column=1)
entry6.grid(row=9,column=1)


entry9.grid(row=10,column=1)
entry10.grid(row=11,column=1)
entry14.grid(row=12,column=1)
entry11.grid(row=13,column=1)
entry12.grid(row=14,column=1)



entry_book_no.delete(0,"end")
entry_book_no.insert(tkinter.END, "67")
entry_book.delete(0,"end")
entry_book.insert(tkinter.END, "윤동주")


#btn8 = Button(tk,text='책번호',bg='black',fg='white',command=search_book).grid(row=0,column=3)
btn8 = Button(tk,text='장절',bg='black',fg='white',command=search_cv).grid(row=1,column=1)
btn1 = Button(tk,text='seq',bg='black',fg='white',command=search_seq).grid(row=2,column=1)

btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=3,column=2)
btn7 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=5,column=2)

btn4 = Button(tk,text='병음',bg='yellow',fg='black',command=trans_china).grid(row=4,column=2)
btn3 = Button(tk,text='삭제',bg='orange',fg='white',command=delete).grid(row=1, column=2)

btn4 = Button(tk,text='히라',bg='yellow',fg='black',command=trans_japan).grid(row=6,column=2)
btn5 = Button(tk,text='수정',bg='blue',fg='white',command=update).grid(row=7,column=2)
btn17 = Button(tk,text='뜻음',bg='black',fg='white',command=trans_korea).grid(row=8,column=2)

btn2 = Button(tk,text='신규',bg='green',fg='white',command=new).grid(row=9,column=2)

btn9 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq_d).grid(row=10,column=1)
btn10 = Button(tk,text='조회',bg='black',fg='white',command=search_hanja_d).grid(row=11,column=1)
btn13 = Button(tk,text='신규',bg='black',fg='white',command=new_d).grid(row=10,column=2)
btn14 = Button(tk,text='삭제',bg='black',fg='white',command=delete_d).grid(row=11,column=2)
btn15 = Button(tk,text='Write',bg='black',fg='white',command=write_d).grid(row=12,column=2)
btn16 = Button(tk,text='수정',bg='black',fg='white',command=update_d).grid(row=13,column=2)


read_d()

def quit():
    write_d()
    tk.quit()


tk.mainloop()

