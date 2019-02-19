#长恨人心不如水，等闲平地起波澜
#!/usr/bin/python
# -*- coding: <encoding name> -*-
import requests

def getHTMLText(url):
    try:
        # kv={'user-agent':'Mozilla/5.0'}
        # kv={'wd':'python'}
        r = requests.get(url)
        r.raise_for_status()#如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r
    except:
        return '产生异常'

def write1(r,path):#将以.jpg的URL保存成图片
    with open(path,'wb') as f:#例path='C:/Users/karvel/Desktop/test3/lubnb'
        f.write(r.content)
        f.close()


if __name__ == '__main__':
    url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1549083409647&di=b228dfdd5cbade69265f9d8efa180644&imgtype=0&src=http%3A%2F%2Fi2.hdslb.com%2Fbfs%2Farchive%2F25c7250e623977513d67065afc2df5f3832bb255.jpg'
    r=getHTMLText(url)
    print(type(r.text))
    #write1(r,path='C:/Users/karvel/Desktop/test3/lubnb')
    #print(type(t))

    #print(t[1000:2000])