import pymysql
import requests as re
from bs4 import BeautifulSoup as bs
# from fake_useragent import UserAgent
# ua = UserAgent()

head = {
        "User-Agent": "Mozilla / 5.0(Macintosh;Intel Mac OS X 11_2_3) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.90 Safari / 537.36"
    }

def getData():
    for i in range(0,250,25):
        url = "https://movie.douban.com/top250?start={}&filter=".format(i)
        r = re.get(url, headers=head)
        code = r.encoding
        content = r.content
        rt = str(content, "utf-8")
        soup = bs(rt, "html.parser")
        try:
            # 序号
            nums = soup.find_all('em')
            titles = soup.find_all('div', class_='hd')
            actors = soup.find_all('p', class_='')
            scores = soup.find_all('span', class_='rating_num')
            # links = soup.select('li div div a')
            links = soup.find_all('div', class_='hd')
            evaluates = soup.find_all('span', class_='inq')
            for n, t, a, s, l, e in zip(nums, titles, actors, scores, links, evaluates):

                id=n.get_text()
                title=t.get_text().split('\n')[2]
                actor=a.get_text().strip()
                score=s.get_text().strip()
                lin=l.find_all('a',class_="")
                link = str(lin[0].get('href'))
                evaluate=e.get_text()
                savenews(id,title,actor,score,link,evaluate)
        except:
            print("error")


def getSummary(link):
    try:
        r = re.get(link, headers=head)
        content = r.content
        rt = str(content, "utf-8")
        soup = bs(rt, 'html.parser')
        summarys = soup.find('div', class_='related-info').find_all('span')
        summary =summarys[0].get_text().strip().replace(" ","")
        return summary
    except:
        print("error")



def savenews(id,title,actor,score,link,evaluate):
    summary = getSummary(link)
    print(summary)

    # pymysql.connect(host,user,password,database )
    db = pymysql.connect(host="localhost", user="root", password="12345678", database="cucnews", charset='utf8')
    cursor = db.cursor()
    try:
        cursor.execute("INSERT INTO douban(id,title,actor,score,link,evaluate,summary) values(%s,%s,%s,%s,"
                "%s,%s,%s)", (id,title,actor,score,link,evaluate,summary))
        print("ok")
        db.commit()
    except:
        print("db-error")
        db.rollback()
    db.close()


getData()
