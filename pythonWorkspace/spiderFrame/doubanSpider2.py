#!/usr/bin/env python
# -*- coding:utf-8

import requests
import re
import selenium.webdriver
import time

#driver=selenium.webdriver.Chrome()

header={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }

def login():

    response=requests.get("https://accounts.douban.com/login",headers=header)

    result=response.text
    print(result)
    reg=r'<img id="captcha_image" src="(.*?)"'
    codeImgUrl=re.findall(reg,result)[0]
    reg=r'<input type="hidden" name="captcha-id" value="(.*?)"/>'
    captchaId=re.findall(reg,result)[0]
    response=requests.get(codeImgUrl,headers=header)
    codeImg=response.content
    fn=open('code.png','wb')
    fn.write(codeImg)
    fn.close()

    print(captchaId)

    captcha_solution=input("请输入验证码:")
    data={
        #这里里面的内容一点点都不能错，区分-,_以及是否与两边有空格
        "source": None,
        "redir": "https://www.douban.com",
        "form_email":"18294434750@163.com",
        "form_password":"dk19950301",
        "captcha-solution":captcha_solution,
        "captcha-id":captchaId,
        "login": "登录",


    }
    #driver.post('https://www.douban.com/accounts/login',data=data,headers=header)
    response2=requests.post('https://www.douban.com/accounts/login',data=data,headers=header)
    print(response2.url)
    #driver.get(response2.url)



login()
