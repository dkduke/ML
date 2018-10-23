# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import os
import random
import time


#应重构成面向对象的代码

# start_url="http://www.budejie.com"
# response =requests.get(start_url)
# print (response.text)

def get_response(url):
    response=requests.get(url).text
    return response#返回网页源代码

#解析包含视频的html
def get_content(html):
    #print(html)
    #re.compile()可写可不写，提升速度的作用
    reg=re.compile(r'(<html>.*?</html>)',re.S)#默认不匹配换行及制表符，故加re.S模式，加了后就可以匹配了
    return re.findall(reg,html)

#获取视频的url地址
def get_mp4_url(response):
    reg=r'<video controls="" width="511" autoplay="true" loop="loop" height="682" src="(.*?)"'
    return re.findall(reg,response)



#<video x-webkit-airplay="allow" webkit-playsinline="" src="http://mvideo.spriteapp.cn/video/2018/0414/5ad14b254eba4_wpcco.mp4"></video>

#获取视频的名字
def get_mp4_name(response,start_url):
    #<title>您的好友👸朵一👯在糖豆发布了一个视频，太好看了</title>
    reg=r'<meta name="Keywords" content="(.*?)" />'#需要我们匹配的用（.*?）
    reg2=r'<h2>(.*?)</h2>'

    user=re.findall(reg2,response)[0]
    curtime=time.strftime('%Y-%m-%d-%H-%M-%S')

    #reg3=r"https://share.tangdou.com/splay.php?vid=(.*?)"
    #strat_url_list=start_url.split()
    #print(strat_url_list)
    #for i in strat_url_list:
        #urlID=re.findall(reg3,i)[0]
    print(start_url)
    urlid=start_url[-13:]
    print(urlid)

    name=user+"--"+re.findall(reg,response)[0]+urlid#findall()返回的是一个list，不管几个元素
    return name




def download_mp4(mp4_url,path):
    path=''.join(path.split())#先分割再拼接
    #.decode('utf-8').encode('gbk')是utf-8到unicoode再到gbk
    path="/Users/dengkun/Downloads/tangdou1/{}.mp4".format(path)
    if not os.path.exists(path):
        urllib.request.urlretrieve(mp4_url,path)#下载，方法一
        print('ok!!!')
        # 方法二  （三行）
        # content =get_response(mp4_url)
        # with open(path,'wb') as f:
        #     f.write(content)
    else:
        print ('NO!!!')

def get_url_name(start_url):
    print(get_content(get_response(start_url)))
    content = get_content(get_response(start_url))
    for i in content:
        print(get_mp4_url(i))
        mp4_url = get_mp4_url(i)
        if mp4_url:
            mp4_name = get_mp4_name(i,start_url)
            print(mp4_name,mp4_url)
            try:
                download_mp4(mp4_url[0], mp4_name)
            except:
                continue


def main():
    #生成器和列表推导式的区别（），【】
    #[get_url_name(start_url) for start_url in start_urls]

    #global start_url
    for start_url in start_urls:
        print(start_url)
        get_url_name(start_url)





if __name__=='__main__' :#判断是不是当前文件执行
    #全局变量
    #view-source:https://share.tangdou.com/splay.php?vid=1500659000014
    #https://share.tangdou.com/splay.php?vid=1500656421261


    start_urls=['https://share.tangdou.com/splay.php?vid={}'.format(urlID) for urlID in range(1500659011000,1500659015000)]
    print(start_urls)
    main()




