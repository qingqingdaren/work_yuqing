from demo1 import reader, reader1
from ..models import Cucnews,DouBan,WakeUp
from . import news
from flask import render_template, request, redirect
from cut2wc import cutwords
from snownlp import SnowNLP
import math


@news.route('/')
def index():
    return redirect('/index')


@news.route('/douban')
def douban():
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = '。'
    rs = list(DouBan.query.filter(DouBan.summary.like('%' + wanted + '%')).all())
    words = ""


    for r in rs:
        words = words + r.summary
    word_c = cutwords(words)
    wordcount = len(word_c)
    # print(word_c)
    return render_template('douban.html', rs=rs, wordcloud=word_c, wordcount=wordcount)

@news.route('/wakeup')
def wakeup():
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = '。'
    rs = list(WakeUp.query.filter(DouBan.summary.like('%' + wanted + '%')).all())
    words = ""


    for r in rs:
        words = words + r.summary
    word_c = cutwords(words)
    wordcount = len(word_c)
    # print(word_c)
    return render_template('wakeup.html', rs=rs, wordcloud=word_c, wordcount=wordcount)


@news.route('/cucnews')
def search():
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = '国家'
    rs = list(Cucnews.query.filter(Cucnews.arti_content.like('%' + wanted + '%')).all())
    # rs_count = Cucnews.query.filter(Cucnews.arti_content.like('%' + wanted + '%')).count()
    words = ""

    for r in rs:
        words = words + r.arti_content
    word_c = cutwords(words)
    wordcount = len(word_c)
    # print(word_c)

    return render_template('cucnews.html', rs=rs, wordcloud=word_c, wordcount=wordcount)


@news.route('/news_result')
def news_result():
    id = request.args.get("id", type=str)
    # print(id)
    if id is None:
        print('no id')
    rs = list(Cucnews.query.filter_by(id=id).all())
    # words = ""
    #
    #
    # for r in rs:
    #     words = words + r.arti_content
    #     print(r.arti_content)
    # word_c = cutwords(words)
    # wordcount = len(word_c)
    # print(word_c)
    return render_template('news_result.html', rs=rs)

@news.route('/daolu')
def daolu():
    # nodes = request.args.get("wanted", type=str)
    # if nodes is None:
    #     wanted = '。'
    # edges=getnodes(nodes)

    nodes=reader()
    edges=reader1()
    return render_template('network1.html',nodes=nodes,edges=edges)


@news.route('/index')
def news():
    wanted = request.args.get("wanted", type=str)
    if wanted is None:
        wanted = ''
    page = int(request.args.get('page', 1))
    # 获取每页显示数据条数默认为2
    per_page = int(request.args.get('perpage', 10))
    # 从数据库查询数据

    paginates = Cucnews.query.filter(Cucnews.arti_content.like('%' + wanted + '%')).paginate(page, per_page,
                                                                                             error_out=False)
    # totalpage为总页面数
    totalpage = math.ceil(paginates.total / per_page)

    word_s=""

    rs = paginates.items
    for r in rs:
        word_s = word_s + r.arti_content
        s = SnowNLP(r.arti_content[:300])
        s.words
        r.sentiments=s.sentiments
        r.keywords=s.keywords()
    word_c = cutwords(word_s)
    wordcount = len(word_c)

    return render_template('index.html',rs=rs, wordcloud=word_c, wordcount=wordcount,paginate = paginates,totalpage = totalpage)


