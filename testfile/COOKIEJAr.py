from urllib import request,parse
from http import cookiejar
#创建cookiejar的实例
cookie = cookiejar.CookieJar()
#生产cookie的管理器
cookie_handler = request.HTTPCookieProcessor()
#创建http请求管理器
http_handler = request.HTTPHandler()
#创建https管理器
https_handler = request.HTTPSHandler()
#创建请求管理器
opener= request.build_opener(http_handler,https_handler,cookie_handler)
def login():
    '''
    负责初次登录
    需要输入用户名密码，用来获取登录cookie凭证
    :return:
    '''
    url = "http://www.renren.com/PLogin.do"
    #此键值需要从登录form的两个对应input中提取name属性
    data = {
        "email":'','13823216623'
        "password":'123456A'
    }
    #把数据进行编码
    data = parse.urlencode(data)
    #创建请求对象
    req = request.Request(url,data=data.encode())
    #使用opener登录
    rsp = opener.open(req)
def getHomePage():
    url = "http://www.renren.com/966912438/profile"
    #如果已经执行了login函数，则opener自动已经包含相 应的cookie值、
    rsp = opener.open(url)
    html = rsp.read().decode()
    with open('rsp.html','w') as f:
        f.write(html)
if __name__ == '__main__':
    login()
    getHomePage()

