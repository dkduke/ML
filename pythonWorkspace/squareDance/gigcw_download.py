# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import os

def get_response(url):
    response=requests.get(url).text
    return response#返回网页源代码

#解析包含视频的html
def get_content(html):
    reg = re.compile(r'(<a href="/v/\d{6}.html" target="_blank" class="pa"><img src=.*? /><em></em>)')
    return re.findall(reg,html)

def get_mp4_first_url(response1):
    reg=r'<a href="(.*?)" target="_blank" class="pa">'
    #print(re.findall(reg,response1))
    return re.findall(reg,response1)

#获取视频的url地址
def get_mp4_url(response2):
    reg=r"var flashvars={f:'(.*?)',p:1};"
    return re.findall(reg,response2)

#获取视频的名字
def get_mp4_name(response1):
    reg = r"alt=\"(.*?)<font color='red'>(.*?)</font>(.*?)\" /><em></em>"
    return re.findall(reg,response1)


def download_mp4(mp4_url,path):
    path="/Users/dengkun/Downloads/squareDance2/{}.mp4".format(path)
    print(path)
    if not os.path.exists(path):
        urllib.request.urlretrieve(mp4_url,path)#下载，方法一
        print('ok!!!')
    else:
        print ('NO!!!')

def get_url_name(start_url):
    content= get_content(get_response(start_url))
    for i in content:
        mp4_url1 = get_mp4_first_url(i)
        second_url="http://www.9igcw.com"+mp4_url1[0]
        print(second_url)
        mp4_url2 = get_mp4_url(get_response(second_url))
        mp4_name =get_mp4_name(i)[0][0]+get_mp4_name(i)[0][1]+get_mp4_name(i)[0][2]
        print(mp4_url2,mp4_name)
        if mp4_url2:
            try:
                download_mp4(mp4_url2[0], mp4_name)
            except:
                continue


def main():
    [get_url_name(start_url) for start_url in start_urls]


if __name__=='__main__' :
    start_urls=['http://www.9igcw.com/e/search/result/index.php?page={}&searchid=29078'.format(i) for i in range(8,11)]
    main()





