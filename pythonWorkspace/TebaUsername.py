#-*— coding:utf-8 -*-
import urllib
import requests
import re
import pymysql
import io
#main

def get_response(url):
    response=requests.get(url).text
    return response#返回网页源代码

def get_username(html):
    #print(html)
    #reg = re.compile(r'<span class="tb_icon_author_rely j_replyer" title="最后回复人:(.*?)">', re.S)
    reg = re.compile(r'<span class="tb_icon_author_rely j_replyer" title="最后回复人:(.*?)">', re.S)
    #reg = re.compile(r'<a rel="noreferrer"  target="_blank" href=".*?" class="topic_name">(.*?)</a>', re.S)
    #reg = re.compile(r'<span class="tb_icon_author_rely j_replyer" title="(.*?)"><i class="icon_replyer"></i>', re.S)
    return re.findall(reg, html)


def write_to_file(file_name,txt):
    print('正在存储文件',file_name)
    f = open(file_name,'w')
    f.write(txt)
    f.close()

def write_to_mysql():
    pass

def tieba_spider(url,begin_page,end_page):
    for i in range(begin_page,end_page+1):
        pn=50*(i-1)
        my_url=url+str(pn)

        html=get_response(my_url)

        file_name=str(i)+'.html'

        nickname=get_username(html)
        print(nickname)

        for i in nickname:
            cursor = conn.cursor()
            #print(type(i))

            params =str(i).replace(' ','')
            #print(params)
            try:
                sql ="insert into nicknames(nickname) values('%s')"%(params)
                print("执行sql语句:" + sql)
                cursor.execute(sql)
                rs = cursor.fetchall()
                print(rs)
                conn.commit()
                cursor.close()
            except:
                print("got exception")






def select_mysql():
    cursor = conn.cursor()
    sql = "select * from nicknames"

    print("执行sql语句:" + sql)
    cursor.execute(sql)
    rs = cursor.fetchall()
    print(rs)
    cursor.close()



if __name__=="__main__":
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', db='DBwork', charset='utf8mb4')

    print()
    url=input('请输入贴吧的URL地址：')

    begin_page=int(input('请输入起始页码'))
    end_page=int(input("请输入终止页码"))

    tieba_spider(url,begin_page,end_page)

    select_mysql()





















