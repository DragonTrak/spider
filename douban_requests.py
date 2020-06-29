import requests


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

session = requests.Session()


def login_page():
    URL_ROOT = 'https://www.douban.com/'
    session.get(URL_ROOT, headers=headers)
    # print(req.text)


def login():
    # 访问登录页
    login_page()
    login_url = 'https://accounts.douban.com/j/mobile/login/basic'
    data = {
        'ck': '',
        'name': '18867249918',
        'password': 'mao5281156',
        'remember': 'false',
        'ticket': ''
    }
    res = session.post(login_url, data=data, headers=headers)
    print(res.json())


def page():
    url = 'https://www.douban.com/'
    res = session.get(url, headers=headers)
    print(res.text)


login()
page()
