from urllib import request, parse, error
import http.cookiejar

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}
# 用来保存cookie
cookie = http.cookiejar.CookieJar()
# 创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
# 通过handler创建opener
opener = request.build_opener(handler)


# 获取登录页 得到cookie
def login_page():
    URL_ROOT = 'https://www.douban.com/'
    req = request.Request(URL_ROOT, headers=headers)
    opener.open(req)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)


def login():
    # 访问登录页
    login_page()
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'ck': '',
        'name': '',
        'password': '',
        'remember': 'false',
        'ticket': ''
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(login_url, data=data, headers=headers)
    try:
        res = opener.open(req)
        print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(e)


def move_page():
    url = 'https://movie.douban.com/'
    req = request.Request(url, headers=headers)
    try:
        res = opener.open(req)
        print(res.read().decode('utf-8'))
    except error.HTTPError as e:
        print(e)


login()
move_page()

