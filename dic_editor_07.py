import json
from tkinter import *
import tkinter.font
import time
import atexit
import pyperclip



tk = Tk()
tk.geometry("510x400+1100+550")
font1 = tkinter.font.Font(family="Consolas", size=12)
tk.title('사전')
tk.wm_attributes("-topmost", 1)


def batch():
    max = len(g_data['dictionary'])

    for j in range(0, max):
            hangul =    g_data['dictionary'][j]['hangul']
            hanja =     g_data['dictionary'][j]['hanja']
            h1 =        g_data['dictionary'][j]['h1']
            h2 =        g_data['dictionary'][j]['h2']
            h3 =        g_data['dictionary'][j]['h3']
            h4 =        g_data['dictionary'][j]['h4']
            h5 =        g_data['dictionary'][j]['h5']
            h6 =        g_data['dictionary'][j]['h6']
            c1 =        g_data['dictionary'][j]['c1']
            c2 =        g_data['dictionary'][j]['c2']
            c3 =        g_data['dictionary'][j]['c3']
            c4 =        g_data['dictionary'][j]['c4']
            c5 =        g_data['dictionary'][j]['c5']
            c6 =        g_data['dictionary'][j]['c6']
            exp =       g_data['dictionary'][j]['exp']
            china =     g_data['dictionary'][j]['china']
            japan =     g_data['dictionary'][j]['japan']
            english =   g_data['dictionary'][j]['english']
            ytube=      "."
            
            new_string = '{ "hangul": "' + hangul + '", "hanja": "' + hanja +'", "h1": "' + h1 + '", "c1": "'+ c1 +'", "h2": "'+ h2 +'", "c2": "'+ c2 +'", "h3": "'+ h3 +'", "c3": "'+ c3 +'", "h4": "'+ h4 +'", "c4": "'+ c4 +'", "h5": "'+ h5 +'", "c5": "'+ c5 +'", "h6": "'+ h6 +'", "c6": "'+ c6 +'", "exp":"'+ exp +'", "china":"'+ china +'", "japan":"'+ japan +'" , "english":"'+ english +'" , "ytube":"'+ ytube +'" }'

            add_json = json.loads(new_string)

            g_data['dictionary'].append(add_json)

    entry01.delete(0,"end")
    entry01.insert(0,"배치완료")

    

def new():

    new_string = '{ "hangul": "X", "hanja": ".", "h1": ".", "c1": ".", "h2": ".", "c2": ".", "h3": ".", "c3": ".", "h4": ".", "c4": ".", "h5": ".", "c5": ".", "h6": ".", "c6": ".", "exp":".", "china":".", "japan":"." , "english":"." , "ytube":"." }'

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
    h1 = entry31.get()
    h2 = entry41.get()
    h3 = entry51.get()
    h4 = entry61.get()
    h5 = entry71.get()
    h6 = entry81.get()
    c1 = entry32.get()
    c2 = entry42.get()
    c3 = entry52.get()
    c4 = entry62.get()
    c5 = entry72.get()
    c6 = entry82.get()
    exp = entry9.get("1.0", "end-1c")
    china = entry10.get()
    china = china.replace("\n", "")
    japan = entry11.get()
    japan = japan.replace("\n", "")
    english = entry12.get()
    english = english.replace("\n", "")
    ytube = entry13.get()
    ytube = ytube.replace("\n", "")

    new_string = '{ "hangul": "' + hangul + '", "hanja": "' + hanja +'", "h1": "' + h1 + '", "c1": "'+ c1 +'", "h2": "'+ h2 +'", "c2": "'+ c2 +'", "h3": "'+ h3 +'", "c3": "'+ c3 +'", "h4": "'+ h4 +'", "c4": "'+ c4 +'", "h5": "'+ h5 +'", "c5": "'+ c5 +'", "h6": "'+ h6 +'", "c6": "'+ c6 +'", "exp":"'+ exp +'", "china":"'+ china +'", "japan":"'+ japan +'" , "english":"'+ english +'" , "ytube":"'+ ytube +'"}'

    add_json = json.loads(new_string)

    g_data['dictionary'].append(add_json)

    entry00.delete(0,"end")

    search_seq()

    entry01.delete(0,"end")
    entry01.insert(0,"카피완료")



def update():

    max = len(g_data['dictionary'])

    seq = int(entry00.get())

    #if(data['dictionary'][seq]['h1'] != "."):
    if(TRUE):
        #print("if")
        for j in range(0, max):
            #print(j)
            if(g_data['dictionary'][seq]['h1'] == g_data['dictionary'][j]['hangul'] ):
                #print(g_data['dictionary'][j]['hangul'])
                g_data['dictionary'][seq]['c1'] = g_data['dictionary'][j]['hanja']
                entry32.delete(0,"end")
                entry32.insert(0,g_data['dictionary'][seq]['c1'])
                break

    #if(g_data['dictionary'][seq]['h2'] != "."):
    if(TRUE):
        for j in range(0, max):
            if(g_data['dictionary'][seq]['h2'] == g_data['dictionary'][j]['hangul'] ):
                g_data['dictionary'][seq]['c2'] = g_data['dictionary'][j]['hanja']
                entry42.delete(0,"end")
                entry42.insert(0,g_data['dictionary'][seq]['c2'])
                break
    
    #if(g_data['dictionary'][seq]['h3'] != "."):
    if(TRUE):
        for j in range(0, max):
            if(g_data['dictionary'][seq]['h3'] == g_data['dictionary'][j]['hangul'] ):
                g_data['dictionary'][seq]['c3'] = g_data['dictionary'][j]['hanja']
                entry52.delete(0,"end")
                entry52.insert(0,g_data['dictionary'][seq]['c3'])
                break

    #if(g_data['dictionary'][seq]['h4'] != "."):
    if(TRUE):
        for j in range(0, max):
            if(g_data['dictionary'][seq]['h4'] == g_data['dictionary'][j]['hangul'] ):
                g_data['dictionary'][seq]['c4'] = g_data['dictionary'][j]['hanja']
                entry62.delete(0,"end")
                entry62.insert(0,g_data['dictionary'][seq]['c4'])
                break

    #if(g_data['dictionary'][seq]['h5'] != "."):
    if(TRUE):
        for j in range(0, max):
            if(g_data['dictionary'][seq]['h5'] == g_data['dictionary'][j]['hangul'] ):
                g_data['dictionary'][seq]['c5'] = g_data['dictionary'][j]['hanja']
                entry72.delete(0,"end")
                entry72.insert(0,g_data['dictionary'][seq]['c5'])
                break
        
    #if(g_data['dictionary'][seq]['h6'] != "."):
    if(TRUE):
        for j in range(0, max):
            if(g_data['dictionary'][seq]['h6'] == g_data['dictionary'][j]['hangul'] ):
                g_data['dictionary'][seq]['c6'] = g_data['dictionary'][j]['hanja']
                entry82.delete(0,"end")
                entry82.insert(0,g_data['dictionary'][seq]['c6'])
                break

    

    g_data['dictionary'][seq]['hangul'] = entry1.get()
    g_data['dictionary'][seq]['hanja'] = entry2.get()
    g_data['dictionary'][seq]['h1'] = entry31.get()
    g_data['dictionary'][seq]['h2'] = entry41.get()
    g_data['dictionary'][seq]['h3'] = entry51.get()
    g_data['dictionary'][seq]['h4'] = entry61.get()
    g_data['dictionary'][seq]['h5'] = entry71.get()
    g_data['dictionary'][seq]['h6'] = entry81.get()
    g_data['dictionary'][seq]['c1'] = entry32.get()
    g_data['dictionary'][seq]['c2'] = entry42.get()
    g_data['dictionary'][seq]['c3'] = entry52.get()
    g_data['dictionary'][seq]['c4'] = entry62.get()
    g_data['dictionary'][seq]['c5'] = entry72.get()
    g_data['dictionary'][seq]['c6'] = entry82.get()
    g_data['dictionary'][seq]['exp'] = entry9.get("1.0", "end-1c")
    temp = entry10.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['china'] = temp
    temp = entry11.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['japan'] = temp
    temp = entry12.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['english'] = temp
    temp = entry13.get()
    temp = temp.replace("\n", "")
    g_data['dictionary'][seq]['ytube'] = temp

    search_seq()
    
    entry01.delete(0,"end")
    entry01.insert(0, "업뎃완료")



def search_hangul():
    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

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
    #entry9.delete(0,"end")
    entry9.delete("1.0", "end-1c")
    entry10.delete(0,"end")
    entry11.delete(0,"end")
    entry12.delete(0,"end")
    entry13.delete(0,"end")

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
            #entry9.insert(0,data['dictionary'][i]['exp'])
            entry9.insert(tkinter.END, data['dictionary'][i]['exp'])
            entry10.insert(0,data['dictionary'][i]['china'])
            entry11.insert(0,data['dictionary'][i]['japan'])
            entry12.insert(0,data['dictionary'][i]['english'])
            entry13.insert(0,data['dictionary'][i]['ytube'])
            break

    



def search_hanja():
    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

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
    #entry9.delete(0,"end")
    entry9.delete("1.0", "end-1c")
    entry10.delete(0,"end")
    entry11.delete(0,"end")
    entry12.delete(0,"end")
    entry13.delete(0,"end")

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
            #entry9.insert(0,data['dictionary'][i]['exp'])
            entry9.insert(tkinter.END, data['dictionary'][i]['exp'])    
            entry10.insert(0,data['dictionary'][i]['china'])
            entry11.insert(0,data['dictionary'][i]['japan'])
            entry12.insert(0,data['dictionary'][i]['english'])
            entry13.insert(0,data['dictionary'][i]['ytube'])
            break

    
def search_each_hanja():
    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

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
                    entry32.delete(0,"end")
                    entry32.insert(0,data['dictionary'][j]['hanja'])
                    break

    if(len(word)>1):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[1] == data['dictionary'][j]['hanja'] ):
                    entry41.delete(0,"end")
                    entry41.insert(0,data['dictionary'][j]['hangul'])
                    entry42.delete(0,"end")
                    entry42.insert(0,data['dictionary'][j]['hanja'])
                    break
        
    if(len(word)>2):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[2] == data['dictionary'][j]['hanja'] ):
                    entry51.delete(0,"end")
                    entry51.insert(0,data['dictionary'][j]['hangul'])
                    entry52.delete(0,"end")
                    entry52.insert(0,data['dictionary'][j]['hanja'])
                    break

    if(len(word)>3):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[3] == data['dictionary'][j]['hanja'] ):
                    entry61.delete(0,"end")
                    entry61.insert(0,data['dictionary'][j]['hangul'])
                    entry62.delete(0,"end")
                    entry62.insert(0,data['dictionary'][j]['hanja'])
                    break

    if(len(word)>4):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[4] == data['dictionary'][j]['hanja'] ):
                    entry71.delete(0,"end")
                    entry71.insert(0,data['dictionary'][j]['hangul'])
                    entry72.delete(0,"end")
                    entry72.insert(0,data['dictionary'][j]['hanja'])
                    break
            
    if(len(word)>5):
            #print("if")
            for j in range(0, max):
                #print(j)
                if(word[5] == data['dictionary'][j]['hanja'] ):
                    entry81.delete(0,"end")
                    entry81.insert(0,data['dictionary'][j]['hangul'])
                    entry82.delete(0,"end")
                    entry82.insert(0,data['dictionary'][j]['hanja'])
                    break

   
    entry01.delete(0,"end")
    entry01.insert(0, "낱자완료")



def next():

    update()

    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

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

    pyperclip.copy(data['dictionary'][i]['hangul'])

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
    #entry9.delete(0,"end")
    entry9.delete("1.0", "end-1c")
    #entry9.insert(0,data['dictionary'][i]['exp'])
    entry9.insert(tkinter.END, data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])
    entry12.delete(0,"end")
    entry12.insert(0,data['dictionary'][i]['english'])
    entry13.delete(0,"end")
    entry13.insert(0,data['dictionary'][i]['ytube'])


def previous():
    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)
    data = g_data

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

    pyperclip.copy(data['dictionary'][i]['hangul'])

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
    #entry9.delete(0,"end")
    entry9.delete("1.0", "end-1c")
    #entry9.insert(0,data['dictionary'][i]['exp'])
    entry9.insert(tkinter.END, data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])
    entry12.delete(0,"end")
    entry12.insert(0,data['dictionary'][i]['english'])
    entry13.delete(0,"end")
    entry13.insert(0,data['dictionary'][i]['ytube'])


def search_seq():
    #with open ("data4.json", "r", encoding = 'utf-8') as f:
    #    data = json.load(f)

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
    #entry9.delete(0,"end")
    #entry9.insert(0,data['dictionary'][i]['exp'])
    entry9.delete("1.0", "end-1c")
    entry9.insert(tkinter.END, data['dictionary'][i]['exp'])
    entry10.delete(0,"end")
    entry10.insert(0,data['dictionary'][i]['china'])
    entry11.delete(0,"end")
    entry11.insert(0,data['dictionary'][i]['japan'])
    entry12.delete(0,"end")
    entry12.insert(0,data['dictionary'][i]['english'])
    entry13.delete(0,"end")
    entry13.insert(0,data['dictionary'][i]['ytube'])

    


def read():
    with open ("data4.json", "r", encoding = 'utf-8') as f:
        data = json.load(f)

    global g_data
    
    g_data = data

    #print(g_data['dictionary'][3])
    
    entry01.delete(0,"end")
    entry01.insert(0, "읽기완료")


def write():

    update()

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

    f = open("data4.json", 'w', encoding = 'utf-8')
    f.write(string)
    f.close()

    #entry00.delete(0,"end")
    #entry00.insert(0, seq)
    entry01.delete(0,"end")
    entry01.insert(0, "저장완료")


def clip_copy():

    temp1_string = entry13.get()

    temp2_string = "<script>\n address = '"

    temp2_string = temp2_string + temp1_string[17:]

    temp2_string = temp2_string + "' \n</script> <div class='tt_article_useless_p_margin contents_style' align='center'>"
    temp2_string = temp2_string + "\n      <div id='player'>&nbsp;</div> <p data-ke-size='size16'>"
    temp2_string = temp2_string + "\n    <script src='https://www.youtube.com/iframe_api'></script>"
    temp2_string = temp2_string + "\n    </p>"
    temp2_string = temp2_string + "\n    <p data-ke-size='size16'>"
    temp2_string = temp2_string + "\n    <script>"
    temp2_string = temp2_string + "\n     var player;"
    temp2_string = temp2_string + "\n      function onYouTubeIframeAPIReady(){"
    temp2_string = temp2_string + "\n        player = new YT.Player('player',{    "
    temp2_string = temp2_string + "\n         videoId: address,        "
    temp2_string = temp2_string + "\n          playerVars:{'autoplay':1,'playsinline':1, 'loop':1},"
    temp2_string = temp2_string + "\n          events:{ 'onReady':onPlayerReady }"
    temp2_string = temp2_string + "\n        });"
    temp2_string = temp2_string + "\n      }"
    temp2_string = temp2_string + "\n      function onPlayerReady(e){	"
    temp2_string = temp2_string + "\n        e.target.mute();"
    temp2_string = temp2_string + "\n        e.target.playVideo();"
    temp2_string = temp2_string + "\n        setTimeout(function(){e.target.unMute()},100);"
    temp2_string = temp2_string + "\n      }"
    temp2_string = temp2_string + "\n    </script>"
    temp2_string = temp2_string + "\n    </p>"
    temp2_string = temp2_string + "\n    </div>"
    temp2_string = temp2_string + "\n    <div id='player'>&nbsp;</div>"
    temp2_string = temp2_string + "\n    <script src='http://www.youtube.com/iframe_api'></script>"
    temp2_string = temp2_string + "\n    <script>"
    temp2_string = temp2_string + "\n      var player;"
    temp2_string = temp2_string + "\n      function onYouTubeIframeAPIReady(){"
    temp2_string = temp2_string + "\n        player = new YT.Player('player',{"
    temp2_string = temp2_string + "\n          width:'100%',        "
    temp2_string = temp2_string + "\n          videoId: address,        "
    temp2_string = temp2_string + "\n          playerVars:{'autoplay':1,'playsinline':1, 'loop':1},"
    temp2_string = temp2_string + "\n          events:{ 'onReady':onPlayerReady }"
    temp2_string = temp2_string + "\n        });"
    temp2_string = temp2_string + "\n      }        "
    temp2_string = temp2_string + "\n      function onPlayerReady(e){"
    temp2_string = temp2_string + "\n        e.target.mute();"
    temp2_string = temp2_string + "\n        e.target.playVideo();"
    temp2_string = temp2_string + "\n      }"
    temp2_string = temp2_string + "\n    </script>"
    temp2_string = temp2_string + "\n    "
    temp2_string = temp2_string + "\n    "

    pyperclip.copy(temp2_string)



def quit():
    write()
    tk.quit()




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
label13 = Label(tk,text='ytube', font=font1).grid(row=13,column=0)

# 각 단위 입력받는 부분 만들기
entry00 = Entry(tk, width=15, font=font1)
entry01 = Entry(tk, width=6, font=font1)
entry1 = Entry(tk, width=40, font=font1)
entry2 = Entry(tk, width=40, font=font1)

entry31 = Entry(tk, width=40, font=font1)
entry41 = Entry(tk, width=40, font=font1)
entry51 = Entry(tk, width=40, font=font1)
entry61 = Entry(tk, width=40, font=font1)
entry71 = Entry(tk, width=40, font=font1)
entry81 = Entry(tk, width=40, font=font1)

entry32 = Entry(tk, width=6, font=font1)
entry42 = Entry(tk, width=6, font=font1)
entry52 = Entry(tk, width=6, font=font1)
entry62 = Entry(tk, width=6, font=font1)
entry72 = Entry(tk, width=6, font=font1)
entry82 = Entry(tk, width=6, font=font1)

entry9 = Text(tk, width=40, height=3, font=font1)
entry10 = Entry(tk, width=40, font=font1)
entry11 = Entry(tk, width=40, font=font1)
entry12 = Entry(tk, width=40, font=font1)
entry13 = Entry(tk, width=40, font=font1)

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
entry12.grid(row=12,column=1)
entry13.grid(row=13,column=1)


btn5 = Button(tk,text='SEQ',bg='black',fg='white',command=search_seq).grid(row=0,column=3)
#btn11 = Button(tk,text='quit',bg='black',fg='white',command=quit).grid(row=1,column=3)
btn2 = Button(tk,text='한글',bg='black',fg='white',command=search_hangul).grid(row=1,column=2)
btn8 = Button(tk,text='한자',bg='black',fg='white',command=search_hanja).grid(row=2,column=2)

btn10 = Button(tk,text='삭제',bg='black',fg='white',command=delete).grid(row=2,column=3)
btn8 = Button(tk,text='낱자',bg='black',fg='white',command=search_each_hanja).grid(row=4,column=3)

btn3 = Button(tk,text='다음',bg='black',fg='white',command=next).grid(row=6,column=3)
btn6 = Button(tk,text='이전',bg='black',fg='white',command=previous).grid(row=8,column=3)

btn4 = Button(tk,text='신규',bg='black',fg='white',command=new).grid(row=9,column=2)
btn7 = Button(tk,text='복사',bg='black',fg='white',command=copy).grid(row=9,column=3)

#btn4 = Button(tk,text='read',bg='black',fg='white',command=read).grid(row=12,column=2)
btn1 = Button(tk,text='수정',bg='black',fg='white',command=update).grid(row=11,column=2)
btn7 = Button(tk,text='write',bg='black',fg='white',command=write).grid(row=11,column=3)

btn21 = Button(tk,text='클립보드',bg='black',fg='white',command=clip_copy).grid(row=13,column=2)

atexit.register(quit)

read()


tk.mainloop()









