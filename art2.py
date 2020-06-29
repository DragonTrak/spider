import requests
import re
from lxml import etree


common_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/51.0.2704.63 Safari/537.36'}

session = requests.Session()


def homePage():
    url = 'http://www.jiangsu.gov.cn/'
    session.get(url)


def get_list():
    default_data = page_spider()
    default_data = default_data.replace('<![CDATA[', '').replace(']]>', '')
    print(default_data)

    xml = etree.XML(default_data)
    total_record = xml.xpath('/datastore/totalrecord/text()')
    print(total_record)
    # 所有a标签
    a_list = xml.xpath('//a')
    for a in a_list:
        if re.match(r'^截至6月', a.text):
            print(a.get('href'))


# 分页查询
def page_spider(startrecord=40, endrecord=50, perpage=20):
    url = 'http://www.jiangsu.gov.cn/module/web/jpage/dataproxy.jsp'
    parms = {
        'startrecord': startrecord,
        'endrecord': endrecord,
        'perpage': perpage
    }
    data = {
        'col': '1',
        'appid': '1',
        'webid': '1',
        'path': '/',
        'columnid': '76936',
        'sourceContentType': '1',
        'unitid': '298841',
        'webname': '江苏省人民政府',
        'permissiontype': '0'
    }

    headers = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/51.0.2704.63 Safari/537.36'}

    res = session.post(url=url, params=parms, data=data, headers=headers)
    xml = str(res.content, 'utf-8')
    return xml


homePage()
get_list()
