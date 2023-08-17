import json


#제이슨 파일 읽어오기

with open ("data2.json", "r", encoding = 'utf-8') as f:
    data = json.load(f)

print(data['dictionary'])

max = len(data['dictionary'])
print(max)
#print(data['dictionary'][0])


#제이슨 데이터 수정

data['dictionary'][0]['hangul'] = "수정"

print(data['dictionary'])


#제이슨 데이터 추가

newrow = { "hangul": "석삼", "hanja": "三" }

data['dictionary'] = data['dictionary'] + [newrow]

print(data['dictionary'])





"""
arr =[]

for i in range(0, max):
    arr.append(data['dictionary'][i]['hangul'])
    arr.append(data['dictionary'][i]['hanja'])

print(arr)
"""





"""

newrow = { "hangul": "두이", "hanja": "二" }

temp = data['dictionary'] + [newrow]

string = json.dumps(temp, ensure_ascii=False)

string = '{"dictionary":' + string + '}'

print(string)




f = open("data2.json", 'w')
f.write(string)
f.close()

"""


