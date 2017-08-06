 payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
 r = requests.get('http://httpbin.org/get', params=payload)
 #print(r.url)
#http://httpbin.org/get?key1=value1&key2=value2&key2=value3

#coding=utf-8
from bs4 import BeautifulSoup
import requests
import uuid
import pymysql
import datetime
import traceback  
#import io
#import sys

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')  
f = open("novel.log","a")
r = requests.get('http://www.feizw.com/Html/12914/index.html')   # 大地产商首页
soup = BeautifulSoup(r.content,"html.parser")
list = soup.select(".chapterlist li a")
conn = pymysql.connect(host='104.140.18.185', port=3306, user='root', passwd='tangdongqing', db='36dsj',charset='utf8')
#conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='36dsj',charset='utf8')
cur = conn.cursor()
list.reverse()
update_articles = []
try:
    for a in list:             
        if(a.get("href") is not None):    #必须要http://格式  and ("http://" in a.get("src")))
            each_data = {}
            detail_url = "http://www.feizw.com/Html/12914/"+a["href"]
            # print(detail_url + a.get_text())
            each_data['article_no']=a.get_text()
            print(detail_url)
            r = requests.get(detail_url)
            soup = BeautifulSoup(r.content,"html.parser")
            content = soup.select_one(".chaptercontent")    # 第一个
            tags = soup.select(".ads_c")
            for tag in tags:
                tag.extract()  #　移除广告标签
            tag2 = soup.select_one(".ads_b")   
            tag2.extract() 
            each_data['article_content'] = content
            # print(content)
            # 根据文章标题查询数据库中是否存在该文章
            sql = "select id,article_no,article_content from david_novel_article where article_no=%s"
            cur.execute(sql,(each_data['article_no'],))
            result = cur.fetchone()
            # print(result)
            if result is not None:
                f.write(detail_url+","+str(datetime.datetime.now())+"\n") #记录日志
                break        # 数据库已经存在数据停止爬取和循环
            update_articles.append(each_data)
except Exception as e:
    print("error as follow:")
    print(e)
    traceback.print_exc()
    #raise Exception
    f.write("network connect failed"+str(e)+str(datetime.datetime.now())+"\n")
finally:
    update_articles.reverse()    # 小说章节从小到大排序
    for each_data in update_articles:
        print(len(update_articles))
        date = datetime.datetime.now()
        sql = "INSERT INTO david_novel_article (id, article_no,article_content,create_time) VALUES (%s, %s,%s,%s)"
        cur.execute(sql,(str(uuid.uuid1()),each_data['article_no'],str(each_data['article_content']),str(date)))
        conn.commit() 
cur.close()
conn.close()
f.close()
    
    
