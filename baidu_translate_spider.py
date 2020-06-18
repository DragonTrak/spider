from urllib import request, parse
import json
'''
百度翻译爬虫demo
'''

url = 'https://fanyi.baidu.com/sug'
# 需要翻译的数据
data = {
    "kw": "decode"
}

# 对数据url编码 并转为byte数组
data = parse.urlencode(data).encode('utf-8')
# 构建请求提
req = request.Request(url, data=data)
# 发起请求
res = request.urlopen(req)
# 读取返回值并解码 utf-8
str = res.read().decode('utf-8')
# 对返回值json序列号
print(json.loads(str))
