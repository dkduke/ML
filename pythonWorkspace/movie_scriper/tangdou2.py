# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import os
import time

def get_response(url):
    response=requests.get(url).text
    return response#返回网页源代码

#解析包含视频的html
def get_content(html):
    reg=re.compile(r'(<div id="cc_video" style="width: 100%; position: relative;">.*?wmode="Opaque" windowlessVideo=1></video>)',re.S)#默认不匹配换行及制表符，故加re.S模式，加了后就可以匹配了
    return re.findall(reg,html)

#获取视频的url地址
def get_mp4_url(response):
    reg=r'src="(.*?)" wmode="Opaque" windowlessVideo=1></video>'
    return re.findall(reg,response)

#获取视频的名字
def get_mp4_name(response,start_url):
    #<title>您的好友👸朵一👯在糖豆发布了一个视频，太好看了</title>
    reg=r'<title>(.*?)</title>'#需要我们匹配的用（.*?）
    curtime=time.strftime('%Y-%m-%d-%H-%M-%S')

    urlid=start_url[-8:]

    name=re.findall(reg,response)[0]+urlid#findall()返回的是一个list，不管几个元素
    return name




def download_mp4(mp4_url,path):
    path=''.join(path.split())
    path="/Users/dengkun/Downloads/tangdou2/{}.mp4".format(path)
    if not os.path.exists(path):
        urllib.request.urlretrieve(mp4_url,path)#下载，方法一
        print('ok!!!')
    else:
        print ('NO!!!')

def get_url_name(start_url):
    #print(get_content(get_response(start_url)))
    content = get_content(get_response(start_url))
    for i in content:
        #print(get_mp4_url(i))
        mp4_url = get_mp4_url(i)
        if mp4_url:
            mp4_name = get_mp4_name(get_response(start_url),start_url)
            print(mp4_name,mp4_url)
            try:
                download_mp4(mp4_url[0], mp4_name)
            except:
                continue


def main():
    #global start_url
    for start_url in start_urls:
        #print(start_url)
        get_url_name(start_url)





if __name__=='__main__' :#判断是不是当前文件执行
    start_urls=['https://share.tangdou.com/play.php?vid={}'.format(urlID) for urlID in range(9011950,9022000)]
    #print(start_urls)
    main()




