import  requests
import html5lib
import re
from bs4 import BeautifulSoup

s=requests.session()
url_login="https://www.douban.com/accounts/login"
url_contacts='https://www.douban.com/people/****/contacts'

formdate={
    'redir':'https://www.douban.com',
    'form_email':'18294434750@163.com',
    'form_password':'dk19950301',
    'login':u'登陆'

}

headers={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

r=s.post(url_login,data=formdate,headers=headers)
content=r.text
#print(content)
soup=BeautifulSoup(content,'html5lib')
captcha=soup.find("img",id='captcha_image')
if captcha:
    captcha_url=captcha['src']
    re_captcha_id=r'<input type-"hidden" name="captcha-id" value="(.*?)"/'
    captcha_id=re.findall(re_captcha_id,content)
    print(captcha_url)
    capthcha_text=input('Please input the captcha:')

    formdate['captcha_soluton']=capthcha_text
    r = s.post(url_contacts, data=formdate, headers=headers)
#r=s.get(url_contacts)
print(r.text)
# with open("contacts.txt",'w+',encoding='utf-8') as f:
#     f.write(r.text)









