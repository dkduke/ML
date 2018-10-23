# _*_ coding:utf-8 _*_

import requests
import re
import urllib
import os
import base64
from pyquery import PyQuery as pq

#应重构成面向对象的代码
class Decode:
    def getHex(self,param1):
        return {
            'str': param1[4:],
            'hex': ''.join(list(param1[:4])[::-1]),
        }


    def getDecimal(self, param1):
        loc2 = str(int(param1, 16))
        # print(loc2)#
        return {
            'pre': list(loc2[:2]),
            'tail': list(loc2[2:]),
        }

    def substr(self, param1, param2):
        loc3 = param1[0: int(param2[0])]
        loc4 = param1[int(param2[0]): int(param2[0]) + int(param2[1])]
        # print("loc4",loc4)
        return loc3 + param1[int(param2[0]):].replace(loc4, "")

    def getPosition(self,param1, param2):
        param2[0] = len(param1) - int(param2[0]) - int(param2[1])
        return param2

    def decode(self, code):
        dict2 = self.getHex(code)
        dict3 = self.getDecimal(dict2['hex'])
        # print("dict3", dict3['pre'])  #
        str4 = self.substr(dict2['str'], dict3['pre'])
        try:
            rlt=base64.b64decode(self.substr(str4, self.getPosition(str4, dict3['tail'])))
        except:
            rlt=''
        print(type(rlt))
        return rlt

    def crawl_video_url(self, url):
        response = requests.get(url).content
        d = pq(response)
        code= d('meta[property="og:video:url"]').attr('content')
        result = self.decode(code)
        return result

def get_response(url):
    response=requests.get(url).text
    return response#返回网页源代码

#解析包含视频的html
def get_content(html):
    #re.compile()可写可不写，提升速度的作用
    reg=re.compile(r'<li class="pr no-select loading  J_media_list_item" .*?>(.*?)</li>',re.S)
    return re.findall(reg,html)


#获取视频的url地址
def get_mp4_url(response):
    # reg=r'data-mp4="(.*?)"'
    # return re.findall(reg,response
    reg=re.compile(r'<span data-href="/media(.*?)" data-sc=""',re.S)
    return re.findall(reg,response)

#获取视频的名字
def get_mp4_name(response):
    # reg=r'<a href="/detail-\d{8}.html">(.*?)</a>'#需要我们匹配的用（.*?）
    # return re.findall(reg,response)#findall()返回的是一个list，不管几个元素
    reg=re.compile(r'class="content-l-p pa" title="(.*?)"')
    print(re.findall(reg,response))
    return re.findall(reg,response)

def download_mp4(mp4_url,path):
    path=''.join(path.split())#先分割再拼接
    #.decode('utf-8').encode('gbk')是utf-8到unicoode再到gbk
    #path="/Users/dengkun/Downloads/budujie_mv/{}.mp4".format(path)
    path = "/Volumes/TOSHIBA\ EXT/mv/{}.mp4".format(path)
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
    content = get_content(get_response(start_url))

    for i in content:
        print(get_mp4_url(i))
        mp4_url = get_mp4_url(i)
        if mp4_url:
            mp4_name = get_mp4_name(i)
            #print(mp4_name,mp4_url)
            try:
                download_mp4_url='http://www.meipai.com/media'+mp4_url[0]
                print('直接获取的url ', download_mp4_url)
                # 获得解码后的视频链接
                v_url = Decode().crawl_video_url(download_mp4_url)
                print('解析后的url',v_url)
                download_mp4(v_url.decode(),mp4_name[0])
            except:
                continue

def main():
    #生成器和列表推导式的区别（），【】
    [get_url_name(start_url) for start_url in start_urls]

if __name__=='__main__' :#判断是不是当前文件执行
    #全局变量
    start_urls=['http://www.meipai.com/search/mv?q=%E7%BE%8E%E5%A5%B3&page={}'.format(i) for i in range(1,40)]
    print(start_urls)
    main()




