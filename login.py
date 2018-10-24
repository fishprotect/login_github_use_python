import setting
import requests
from lxml import etree


class Login(object):
    def __init__(self):
        self.url_auth_token = "https://github.com/login"
        self.post_url = "https://github.com/session"
        self.header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
        self.session = requests.Session()
        print("初始化。。。。。")
    def get_authenticity_token(self):
        try:
            con = self.session.get(self.url_auth_token,headers = self.header)
            if con.status_code != 200:
                print("1提取 authenticity_token 出错")
                exit() 
        except:
            print("2提取 authenticity_token 出错")
            exit()
        print("访问login页面完成。。。。。。")
        html = etree.HTML(con.text)
        result = html.xpath('//input[@name="authenticity_token"]/@value')[0]
        print("完成authenticity_token的提取")
        return result
    def login(self,user,pwd):
        data = {
                'commit':'Sign in',
                'utf8':'✓',
                'login':user,
                'password':pwd,
                'authenticity_token':self.get_authenticity_token()
            }
        print("data 提取完毕。。。。。")
        try:
            response = self.session.post(self.post_url,headers=self.header,data = data)
            if response.status_code==200:
                print("完成登陆")
            else:
                print("密码用户名可能不正确，请重新配置")
                exit()
        except:
            print("密码用户名可能不正确，请重新配置")
            exit()
        with open("login_git.html","w") as f:
            f.write(response.text)
        print('首页已经保存为login_git.html')
if __name__=="__main__":
    user = setting.USER
    pwd  = setting.PWD
    login = Login()
    login.login(user=user,pwd=pwd)
