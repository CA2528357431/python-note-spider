# REQUEST


import requests

header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
url="https://www.baidu.com"
r=requests.get(url,headers=header)
string=r.text



# bs


import bs4
import lxml

soup=bs4.BeautifulSoup(string,"lxml")
#print(soup)



# find

#result=soup.find("head")
#print(result)
#result=soup.find(attrs={"data-compress":"strip"})
#print(result)
#result=soup.find(text="百度一下，你就知道")
#print(result)      -----这个几乎不用


# json


import json


#json-->python

jsonstr='''[
  {
    "name" : "曹安",
    "age" : 29,
    "secretIdentity" : "Dan Jukes",
    "powers" : [
      "Radiation resistance",
      "Turning tiny",
      "Radiation blast"
    ]
  },
  {
    "name" : "Madame Uppercut",
    "age" : 39,
    "secretIdentity" : "Jane Wilson",
    "powers" : [
      "Million tonne punch",
      "Damage resistance",
      "Superhuman reflexes"
    ]
  }
]'''
jsonstr_r=json.loads(jsonstr)#内存中的数据loads
#print(jsonstr_r)

jsonstr=open("test1.json")
jsonstr_r=json.load(jsonstr)#储存中的数据load
#print(jsonstr_r)


#python-->json

jsonstr_rr=json.dumps(jsonstr_r)
#print(jsonstr_rr)#中文不可

jsonstr_rrch=json.dumps(jsonstr_r,ensure_ascii=False)
#print(jsonstr_rrch)#中文可

x=open("test2.json","w")
json.dump(jsonstr_r,x,ensure_ascii=False)

#re

import re

find=re.compile("ab(.*)d(.*)z")
find0=re.compile("ab.*d.*z")
st="abcdezfc"
sss=find.findall(st)
print(sss)
sss=find0.findall(st)
print(sss)

