import requests
import regex
import re
import random
import sys
import time as t
from DataIO import insert
from bs4 import BeautifulSoup
for page in range(579,1000):
    url = "https://www.yidaiyilu.gov.cn/info/iList.jsp?cat_id=10002&cur_page="+str(page)
    t.sleep(20)
    payload = {}
    headers = {
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36',
      'Cookie': '__jsluid_h=4e55df1e87a7bcad13077163bef19704; __jsluid_s=3cad65f0bf5c6574890ad66851273ab7; Lmlist=1%2C2%2C3%2C4%2C5%2C6%2C7%2C8; security_session_verify=1873f554429a2bf7c9099f429ce42769; insert_cookie=65472086; __jsl_clearance=1600968636.347|0|85G3UjYdRu0iQbyL9iQPGTIGUUs%3D'
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    soup=BeautifulSoup(response.text,'html.parser')
    herf=soup.find_all(href=re.compile('gnxw'))
    List=[]
    pattern=regex.compile('\/x.*?m')
    for i in herf:
        h=pattern.findall(str(i))
        for j in h:
            link='https://www.yidaiyilu.gov.cn'+j
            if link not in List:
                List.append(link)
    print('爬至第'+str(page)+'页')    # 通过新闻页获得当前页新闻链接
    print(List)
    if not List:
        filename = 'log.txt'
        with open(filename, 'a') as file_object:
            file_object.write('爬至第' + str(page) + '页中断\n')  # cookies失效时记录爬虫位置
        print('爬至第' + str(page) + '页中断\n')
        sys.exit()
    # List=['https://www.yidaiyilu.gov.cn/xwzx/gnxw/149482.htm', 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/149389.htm', 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/149393.htm', 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/149403.htm', 'https://www.yidaiyilu.gov.cn/xwzx/gnxw/149413.htm']
    for i in range(len(List)):
        t.sleep(random.randint(2,5))
        newsresponse = requests.request("GET", List[i], headers=headers, data = payload)
        newsresponse.encoding='utf-8'

        newssoup=BeautifulSoup(newsresponse.text,'html.parser')
        if not newssoup.find('title') or not newssoup.find(class_='main_content_date szty1') or not newssoup.find(class_='main_content_date szty2') or not newssoup.find(class_='info_content'):
            filename = 'log.txt'
            with open(filename, 'a') as file_object:
                file_object.write("新闻:"+List[i]+"格式不正确,请手动检查\n")  # cookies失效时记录爬虫位置
            print("新闻:"+List[i]+"格式不正确")
            continue
        title=str(newssoup.find('title'))[7:-18] #获取新闻标题

        time=str(newssoup.find(class_='main_content_date szty1'))
        time=re.findall('>.*?<',time)[0][1:-1]  #获取新闻时间

        source=str(newssoup.find(class_='main_content_date szty2'))
        source=re.findall('>.*?<',source)[0][4:-1]   #获取新闻来源

        content=str(newssoup.find(class_='info_content'))
        content=re.sub('<[^<]+?>','',content).replace('\n','')


        values=(List[i],title,time,source,content)
        print(values)
        insert(values)