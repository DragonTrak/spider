import requests


headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__jsluid_h=c15381367a37333dd96c96fd7bd81ca4; zh_choose_1=s; yunsuo_session_verify=31b594c5b62062e48b0b5216f1ae1f3d',
    'Host': 'www.jiangsu.gov.cn',
    'If-Modified-Since': 'Sat, 13 Jun 2020 01:33:52 GMT',
    'If-None-Match': 'W/2c49-5a7ed2fa54000',
    'Referer': 'http://www.jiangsu.gov.cn/col/col76936/index.html?uid=298841&pageNum=2',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
res = requests.get('http://www.jiangsu.gov.cn/art/2020/6/2/art_76936_9193328.html', headers=headers)

print(str(res.content, 'utf-8'))