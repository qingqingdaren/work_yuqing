import pymysql
import requests as re
from bs4 import BeautifulSoup as bs
# from fake_useragent import UserAgent
# ua = UserAgent()
import random

head = {
        "User-Agent": "Mozilla / 5.0(Macintosh;Intel Mac OS X 11_2_3) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.90 Safari / 537.36"
    }
def getData():

    for i in range(0,372,20):
        url = "https://movie.douban.com/subject/30228394/reviews?start={}".format(i)
        r = re.get(url, headers=head)
        # r = re.get(url, headers={'User-Agent':random.choice(user_agent)})
        code = r.encoding
        content = r.content
        rt = str(content, "utf-8")
        soup = bs(rt, "html.parser")
        # print(soup)
        h2=soup.find_all('h2')
        try:
            for h in h2:

                title= h.get_text()
                links = h.find_all('a')
                link=str(links[0].get('href'))
                content = getSummary(link)
        #
                savenews(title,link,content)
        except Exception as e:
            print(e)
            print("error")

# # link="https://movie.douban.com/review/13266996/"
def getSummary(link):
    try:
        r = re.get(link, headers=head)
        content = r.content
        rt = str(content, "utf-8")
        soup = bs(rt, 'html.parser')
        #print(soup)
        summarys = soup.find('div', class_='review-content clearfix')
        content=summarys.get_text().strip().replace(" ","")
        # print(content)
#         summary =summarys[0].get_text().strip().replace(" ","")
        return content
    except Exception as e:
        print(e)
        print("error")
# # getSummary(link)
# #
# #
def savenews(title,link,content):
     content = getSummary(link)
# #     print(summary)
# #
     db = pymysql.connect(host="localhost", user="root", password="12345678", database="cucnews", charset='utf8')
     cursor = db.cursor()
     try:
         cursor.execute("INSERT INTO wakeup(title,link,content) values(%s,%s,%s)", (title,link,content))
         print("ok")
         db.commit()
     except Exception as e:
         print(e)
         print("db-error")
         db.rollback()
     db.close()


getData()

