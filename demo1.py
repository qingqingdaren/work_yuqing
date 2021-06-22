import csv
from flask import request

def reader():
    namelist={}
    nodes=[]
    with open('/Users/fairy/PycharmProjects/爬虫4/name.csv', 'r') as f:
        reader = csv.reader(f, delimiter='\n')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
        for row in reader:
            nodes.append({"name":row[0]})
        print(nodes)
    return nodes
reader()

def reader1():
    namelist={}
    edges=[]
    with open('/Users/fairy/PycharmProjects/爬虫4/out.csv', 'r') as f:
        reader = csv.reader(f, delimiter=' ')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
        for row in reader:
            edges.append({"source":int(row[0])-1,"target":int(row[1])-1})
        print(edges)
    return edges
reader1()

def getnodes(nodes):
    edges=[]
    with open('/Users/fairy/PycharmProjects/爬虫4/out.csv', 'r') as f:
        reader = csv.reader(f, delimiter=' ')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
        for row in reader:
            if (row[0]==nodes) or (row[1]==nodes):
                edges.append({"source": int(row[0]) - 1, "target": int(row[1]) - 1})
    return edges

def search():
    core = request.args.get("core", type=str)
    if core is None:
        core = 1
        print('edges')