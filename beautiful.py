#长恨人心不如水，等闲平地起波澜

import requests
import bs4
from bs4 import BeautifulSoup
import re

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()#如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''


def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, 'html.parser')#固定格式
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):#检测标签类型
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])
    pass

def printUnivLidt(ulist, num):
    print('{:^10}\t{:^6}\t{:^10}'.format('排名', '大学', '总分'))
    for i in range(num):
        u =ulist[i]
        print('{:^10}\t{:^6}\t{:^10}'.format(u[0],u[1],u[2]))
    #print('Suc'+str(num))

#re淘宝链接部分
def parsePage(ilt,html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        tlt = re.findall(r'\'raw_title\'\:\'.*?''',html)
print('')

def printGoodsList(ilt):
   print('')

def main1():
    uinfo = []
    url ='http://www.zuihaodaxue.com/zuihaodaxuepaiming2018.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivLidt(uinfo, 20)#显示20个数据

def main2():
    goods = '书包'
    depth = 2
    start_url = 'https://s.taobao.com/search?q='+ goods
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s='+ str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    printGoodsList(infoList)

#main2()