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




def search2_old(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan'] 
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan'] 
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan'] 
                    break      
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan'] 
                    break      
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul'] + "    " + data['dictionary'][i]['china'] + "    " + data['dictionary'][i]['japan'] 
                    break      
                else: 
                    i = i + 1

        return temp4


def search_hanja(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break        
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break        
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hanja']
                    break       
                else: 
                    i = i + 1

        return temp4


def search_hangul(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break        
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break        
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['hangul']
                    break       
                else: 
                    i = i + 1

        return temp4


def search_china(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break        
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break        
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['china']
                    break       
                else: 
                    i = i + 1

        return temp4


def search_japan(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break        
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break        
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['japan']
                    break       
                else: 
                    i = i + 1

        return temp4


def search_english(): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = pyperclip.paste()


        word = list(temp)
        temp4 = ""

        # 1글자 조회

        if(len(word)>0 and len(word)<2):

            temp2 = word[0]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break      
                else: 
                    i = i + 1

        # 2글자 조회

        if(len(word)>1 and len(word)<3):

            temp2 = word[0] + word[1]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break      
                else: 
                    i = i + 1

        # 3글자 조회

        if(len(word)>2 and len(word)<4):

            temp2 = word[0] + word[1] + word[2]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break      
                else: 
                    i = i + 1

        # 4글자 조회

        if(len(word)>3 and len(word)<5):

            temp2 = word[0] + word[1] + word[2] + word[3]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break        
                else: 
                    i = i + 1

        # 5글자 조회

        if(len(word)>4 and len(word)<6):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break        
                else: 
                    i = i + 1

        # 6글자 조회

        if(len(word)>5 and len(word)<7):

            temp2 = word[0] + word[1] + word[2] + word[3] + word[4] + word[5]

            for i in range(max):
                if(temp2 == data['dictionary'][i]['hanja'] or temp2 == data['dictionary'][i]['hangul']):
                    temp4 = data['dictionary'][i]['english']
                    break       
                else: 
                    i = i + 1

        return temp4



def search20(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 0):

            temp3 = word[0]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search30(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 1):

            temp3 = word[1]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search40(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 2):

            temp3 = word[2]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search50(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 3):

            temp3 = word[3]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4


def search60(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 4):

            temp3 = word[4]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4


def search70(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 5):

            temp3 = word[5]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['hanja'] + " " + data['dictionary'][i]['hangul']         
                    break      
                else: 
                    i = i + 1

        return temp4


def search21(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 0):

            temp3 = word[0]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search31(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 1):

            temp3 = word[1]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search41(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 2):

            temp3 = word[2]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']    
                    break      
                else: 
                    i = i + 1

        return temp4

def search51(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 3):

            temp3 = word[3]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']       
                    break      
                else: 
                    i = i + 1

        return temp4


def search61(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 4):

            temp3 = word[4]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']        
                    break      
                else: 
                    i = i + 1

        return temp4


def search71(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 5):

            temp3 = word[5]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['china']       
                    break      
                else: 
                    i = i + 1

        return temp4


def search22(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 0):

            temp3 = word[0]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search32(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 1):

            temp3 = word[1]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']         
                    break      
                else: 
                    i = i + 1

        return temp4

def search42(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 2):

            temp3 = word[2]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']    
                    break      
                else: 
                    i = i + 1

        return temp4

def search52(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 3):

            temp3 = word[3]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']       
                    break      
                else: 
                    i = i + 1

        return temp4


def search62(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 4):

            temp3 = word[4]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']        
                    break      
                else: 
                    i = i + 1

        return temp4


def search72(temp_hanja): 
        with open ("data3.json", "r", encoding = 'utf-8') as f:
            data = json.load(f)

        max = len(data['dictionary'])

        temp = temp_hanja
        #print(temp)
        word = list(temp)
        temp4 = ""

        # 2-0글자 조회

        if(len(word) > 5):

            temp3 = word[5]
         
            for i in range(max):
                if(temp3 == data['dictionary'][i]['hanja']):
                    temp4 = data['dictionary'][i]['japan']       
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
        self.root.geometry("611x171-70-10")       # 창 크기설정
        self.root.title("dictionary")    # 창 제목설정
        self.root.option_add("*Font","맑은고딕 11") # 폰트설정
        self.root.resizable(False, False)  # x, y 창 크기 변경 불가

        self.ent00 = Entry(self.root, width=25)
        self.ent10 = Entry(self.root, width=25)            
        self.ent20 = Entry(self.root, width=25)                 
        self.ent30 = Entry(self.root, width=25)                 
        self.ent40 = Entry(self.root, width=25)                   
        self.ent50 = Entry(self.root, width=25)   
        self.ent60 = Entry(self.root, width=25)
        self.ent70 = Entry(self.root, width=25)
        self.ent80 = Entry(self.root, width=25)       

        self.ent01 = Entry(self.root, width=25)
        self.ent11 = Entry(self.root, width=25)            
        self.ent21 = Entry(self.root, width=25)                 
        self.ent31 = Entry(self.root, width=25)                 
        self.ent41 = Entry(self.root, width=25)                   
        self.ent51 = Entry(self.root, width=25)   
        self.ent61 = Entry(self.root, width=25) 
        self.ent71 = Entry(self.root, width=25) 
        self.ent81 = Entry(self.root, width=25) 

        self.ent02 = Entry(self.root, width=25)
        self.ent12 = Entry(self.root, width=25)            
        self.ent22 = Entry(self.root, width=25)                 
        self.ent32 = Entry(self.root, width=25)                 
        self.ent42 = Entry(self.root, width=25)                   
        self.ent52 = Entry(self.root, width=25)   
        self.ent62 = Entry(self.root, width=25)  
        self.ent72 = Entry(self.root, width=25)   
        self.ent82 = Entry(self.root, width=25)        

        self.ent00.grid(row=0,column=0)  #한자
        self.ent02.grid(row=0,column=1)  #공백
        self.ent01.grid(row=0,column=2)  #영어
        self.ent10.grid(row=1,column=0)  #한글
        self.ent11.grid(row=1,column=1)  #중국어
        self.ent12.grid(row=1,column=2)  #일본어


        self.ent80.grid(row=2,column=0) 
        self.ent20.grid(row=3,column=0) 
        self.ent30.grid(row=4,column=0) 
        self.ent40.grid(row=5,column=0) 
        self.ent50.grid(row=6,column=0)    
        self.ent60.grid(row=7,column=0)    
        self.ent70.grid(row=8,column=0)          



        self.ent81.grid(row=2,column=1) 
        self.ent21.grid(row=3,column=1) 
        self.ent31.grid(row=4,column=1) 
        self.ent41.grid(row=5,column=1) 
        self.ent51.grid(row=6,column=1)    
        self.ent61.grid(row=7,column=1)  
        self.ent71.grid(row=8,column=1) 

        self.ent82.grid(row=2,column=2) 
        self.ent22.grid(row=3,column=2) 
        self.ent32.grid(row=4,column=2) 
        self.ent42.grid(row=5,column=2) 
        self.ent52.grid(row=6,column=2)    
        self.ent62.grid(row=7,column=2)   
        self.ent72.grid(row=8,column=2)  




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

            temp99 = l_check

            self.ent00.delete(0, "end")
            temp_hanja = search_hanja()
            self.ent00.insert(0, temp_hanja)
            self.ent10.delete(0, "end")
            self.ent10.insert(0, search_hangul())
            self.ent11.delete(0, "end")
            self.ent11.insert(0, search_china())
            self.ent12.delete(0, "end")
            self.ent12.insert(0, search_japan())
            self.ent01.delete(0, "end")
            self.ent01.insert(0, search_english())
            
            self.ent20.delete(0, "end")
            self.ent20.insert(0, search20(temp_hanja))
            self.ent30.delete(0, "end")
            self.ent30.insert(0, search30(temp_hanja))
            self.ent40.delete(0, "end")
            self.ent40.insert(0, search40(temp_hanja))
            self.ent50.delete(0, "end")
            self.ent50.insert(0, search50(temp_hanja))
            self.ent60.delete(0, "end")
            self.ent60.insert(0, search60(temp_hanja))
            self.ent70.delete(0, "end")
            self.ent70.insert(0, search70(temp_hanja))

            self.ent21.delete(0, "end")
            self.ent21.insert(0, search21(temp_hanja))
            self.ent31.delete(0, "end")
            self.ent31.insert(0, search31(temp_hanja))
            self.ent41.delete(0, "end")
            self.ent41.insert(0, search41(temp_hanja))
            self.ent51.delete(0, "end")
            self.ent51.insert(0, search51(temp_hanja))
            self.ent61.delete(0, "end")
            self.ent61.insert(0, search61(temp_hanja))
            self.ent71.delete(0, "end")
            self.ent71.insert(0, search71(temp_hanja))

            self.ent22.delete(0, "end")
            self.ent22.insert(0, search22(temp_hanja))
            self.ent32.delete(0, "end")
            self.ent32.insert(0, search32(temp_hanja))
            self.ent42.delete(0, "end")
            self.ent42.insert(0, search42(temp_hanja))
            self.ent52.delete(0, "end")
            self.ent52.insert(0, search52(temp_hanja))
            self.ent62.delete(0, "end")
            self.ent62.insert(0, search62(temp_hanja))
            self.ent72.delete(0, "end")
            self.ent72.insert(0, search72(temp_hanja))
            
                        
        self.root.after(1000, self.update_clock)

app=Clock()