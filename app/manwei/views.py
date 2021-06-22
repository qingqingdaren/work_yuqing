# from demo1 import reader, reader1
from ..models import Cucnews, DouBan
from . import news
from flask import render_template, request, redirect
from cut2wc import cutwords
import math
from app.manwei.manweidemo import spider


@news.route('/')
def index():
    return redirect('/index')


@news.route('/douban')
def douban():
    wanted = request.args.get("wanted", type=str)
    page = request.args.get("page", type=int)
    if page is None:
        page = 0
    if wanted is None:
        wanted = '。'

    rs = list(DouBan.query.filter(DouBan.summary.like('%' + wanted + '%')).all())
    words = ""
    totalpage = math.ceil(len(rs) / 10)

    for r in rs:
        words = words + r.summary
    word_c = cutwords(words)
    wordcount = len(word_c)
    rs = list_split(rs, 10)

    res = rs[page]
    return render_template('douban.html', rs=res, wordcloud=word_c, wordcount=wordcount,page=page,totalpage=totalpage)


# 切分数组
def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


@news.route('/cucnews')
def search():

    wanted = request.args.get("wanted", type=str)
    page = request.args.get("page", type=int)
    if page is None:
        page = 0
    if wanted is None:
        wanted = '。'
    news = list(Cucnews.query.filter(Cucnews.arti_content.like('%' + wanted + '%')).all())
    words = ""
    # totalpage为总页面数
    totalpage = math.ceil(len(news) / 10)

    for r in news:
        words = words + r.arti_content


    word_c = cutwords(words)
    wordcount = len(word_c)
    news = list_split(news, 10)

    res = news[page]

    return render_template('news_list.html', news=res,wordcloud=word_c, wordcount=wordcount,page=page,totalpage=totalpage)


@news.route('/news_result')
def news_result():
    id = request.args.get("id", type=str)
    if id is None:
        print('no id')
    rs = list(Cucnews.query.filter_by(id=id).all())
    return render_template('news_detail.html', rs=rs)


@news.route('/manwei')
def manwei():
    # lstt = [0, 17, 3, 6, 41, 54, 113, 1, 2]
    name = request.args.get("name", type=str)
    if name is None:
        name="tonys"
    nodes, edges = spider(name)
    return render_template('manwei.html',nodes=nodes,edges=edges)

@news.route('/index')
def news():
    return render_template('index.html')
