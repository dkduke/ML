# -*- coding: UTF-8 -*-

import sys
import time
import requests
import hashlib
import os,shutil
import time
import json
import subprocess
from multiprocessing import Process
from multiprocessing import Pool
import multiprocessing
import re

##糖豆 640x360
tdpng640shuiyin = "\"movie=td153x39_477x8.png[watermark];[in][watermark]overlay=477:8:0[out]\""
##糖豆MV 960x720  需要更新
tdpng960shuiyin = "\"movie=td153x39_477x8.png[watermark];[in][watermark]overlay=447:17:0[out]\""
##就爱 640x360
jipng640shuiyin = "\"movie=ji182x38_447x17.png[watermark];[in][watermark]overlay=447:17:0[out]\""
##就爱 1024x576  需要更新
jipng1024shuiyin = "\"movie=ji134x28_497x12.png[watermark];[in][watermark]overlay=497:12:0[out]\""

source = "D:\\dancevideo\\all_down\\9i\\fenlei\\健身操\\"
dest = []
# ffmpeg.exe -ss 00:00:16 -i test.mp4 -t 00:02:00 -c:a aac  -ac 2 -ar 48000 -b:a 128k  -c:v libx264 -crf 20 -s 360x480 -r 20 -bf 2 -keyint_min 20 -g 40 -s 640x360 -movflags faststart -vf "movie=td153x39_477x8.png[watermark];[in][watermark]overlay=447:17:0[out]" testout.mp4
def task640td(msg):
     a = subprocess.call("ffmpeg.exe -ss 00:00:08 -i {3}{0} -c:a aac  -ac 2 -ar 48000 -b:a 128k  -c:v libx264 -crf 20 -s 640x360 -r 20 -bf 2 -keyint_min 20 -g 40 -movflags faststart -vf {4} {1}{2}".format(msg,dest,msg,source,tdpng640shuiyin),shell=True)
def task640ji(msg):
     a = subprocess.call("ffmpeg.exe -ss 00:00:15 -i {3}{0} -c:a aac  -ac 2 -ar 48000 -b:a 128k  -c:v libx264 -crf 20 -s 640x360 -r 20 -bf 2 -keyint_min 20 -g 40 -movflags faststart -vf {4} {1}{2}".format(msg,dest,msg,source,jipng640shuiyin),shell=True)
def task960tdMV(msg):
     a = subprocess.call("ffmpeg.exe -ss 00:00:08 -i {3}{0} -c:a aac  -ac 2 -ar 48000 -b:a 128k  -c:v libx264 -crf 20 -s 360x480 -r 20 -bf 2 -keyint_min 20 -g 40 -movflags faststart -vf {4} {1}{2}".format(msg,dest,msg,source,tdpng960shuiyin),shell=True)
def task1024ji(msg):
     a = subprocess.call("ffmpeg.exe -ss 00:00:15 -i {3}{0} -c:a aac  -ac 2 -ar 48000 -b:a 128k  -c:v libx264 -crf 20 -s 640x360 -r 20 -bf 2 -keyint_min 20 -g 40 -movflags faststart -vf {4} {1}{2}".format(msg,dest,msg,source,jipng1024shuiyin),shell=True)

def get_rate(msg):
     output = subprocess.Popen("ffprobe.exe -print_format json -show_streams {1}{0}".format(msg,source),shell=True,stdout=subprocess.PIPE)
     oc=output.communicate()[0]
     oc1 = bytes.decode(oc)
     return oc1

dest =  source[0:-1]+"_new\\"
#print (dest)
if not os.path.exists(dest):
    os.makedirs(dest)                #创建路径

list2 = []
list1 = []
list2 = os.listdir(source)
#print (list2)

for i in list2:
    name = re.sub('\s','',i)
    source_name = source + i
    dest_name = source + name
    name_tmp = os.rename(source_name,dest_name)
    list1.append(name_tmp)


td = 0
tdmv = 0
ji = 0
iother=0
list2 = os.listdir(source)

filetype ='.mp4' #指定文件类型
name =[]
final_name = []
for i in list2:
    if filetype in i:
        name.append(i.replace(filetype,''))#生成不带‘filetype’后缀的文件名组成的列表
    else:
        shutil.move(source+i,dest+i)
list2 = [item +filetype for item in name]#生成‘filetype’后缀的文件名组成的列表

#print (list2)

for i in list2:
     if not i.strip():
         pass
     else:
         tmp = get_rate(msg=i)
         tmp1 = json.loads(tmp)
         if int(tmp1["streams"][0]["width"]) == 640:
            if int(tmp1["streams"][0]["height"]) == 360:
                #print (tmp1["streams"][0]["width"])
                #task640td(msg=i)
                task640ji(msg=i)
                td = td+1
         else:
             if int(tmp1["streams"][0]["width"]) == 1024:
                if int(tmp1["streams"][0]["height"]) == 576:
                    #print (tmp1["streams"][0]["width"])
                    task1024ji(msg=i)
                    ji = ji+1
             else:
                 if int(tmp1["streams"][0]["width"]) == 720:
                    if int(tmp1["streams"][0]["height"]) == 960:
                        #print (tmp1["streams"][0]["width"])
                        task960tdMV(msg=i)
                        tdmv = tdmv+1
                 else:
                    #print (tmp1["streams"][0]["width"])
                    iother = iother+1
print (td)
print (tdmv)
print (iother)




