#-*- coding:utf-8 -*-
'''
Created on Jun 29, 2018

@author: dengkun
'''
import requests
import time

url='https://api.live.bilibili.com/ajax/msg'

dat={'csrf_token':' ',
'roomid':'3066386',
'visit_id':'4rwf91pwx0n4'}

# bulletScreens=dates.json()['data']['room']
# #print(bulletScreens)
# for bs in bulletScreens:
#     print(bs['text'])
count=0
lists=[]


try:
    while count<10000:
        time.sleep(2)
        dates = requests.post(url, data=dat)
        bulletScreens=list(map(lambda ii:dates.json()['data']['room'][ii]['text'],range(10)))
        time.sleep(3)
        lists=list(set(lists+bulletScreens))
        #print(bulletScreens)
        count=len(lists)
        print(count)
except Exception:
    print('error')
fl = open('list.txt', 'w+')
for i in lists:
    fl.write(i)
    fl.write("\n")
fl.close()

