import requests
import pandas as pd


# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
# pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 100)

# 用session管理会话
session = requests.session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}


# 访问登录页
def login_page():
    url_root = 'https://www.douban.com/'
    session.post(url_root, headers=headers)


# 登录豆瓣
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
    print(res.text)


# 热门电影爬取
def hot_movie():
    url = 'https://movie.douban.com/j/search_subjects'
    params = {
        'type': 'movie',
        'tag': '热门',
        'page_limit': 50,
        'page_start': 0
    }
    res = session.get(url, params=params, headers=headers)
    save_hot_movie(res.json())


# 保存数据
def save_hot_movie(json_str):
    subjects = json_str['subjects']
    print(subjects)
    df = pd.DataFrame(data=subjects)
    df.set_index('id', inplace=True)
    df.to_csv('top_movie.csv')


hot_movie()
