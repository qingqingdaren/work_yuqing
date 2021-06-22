import numpy as np
import csv
import networkx as nx
import operator
from urllib import request
from math import sqrt
from pygraph.classes.digraph import digraph
import matplotlib.pyplot as plt #导入科学绘图包
from scipy.interpolate import make_interp_spline

headers = {
            "User-Agent": "Mozilla / 5.0(Macintosh;Intel Mac OS X 11_2_3) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 89.0.4389.90 Safari / 537.36"
        }
#下载节点人物图片
def down_pic(url, path):
    try:
        req = request.Request(url, headers=headers)
        data = request.urlopen(req).read()
        with open(path, 'wb') as f:
            f.write(data)
            f.close()
    except Exception as e:
        print(str(e))

# class HITSIterator:
#     # __doc__ = '''计算一张图中的hub,authority值'''
#
#     def __init__(self, dg):
#         self.max_iterations = 100  # 最大迭代次数
#         self.min_delta = 0.0001  # 确定迭代是否结束的参数
#         self.graph = dg
#
#         self.hub = {}
#         self.authority = {}
#         for node in self.graph.nodes():
#             self.hub[node] = 1
#             self.authority[node] = 1
#
#     def hits(self):
#         """
#         计算每个页面的hub,authority值
#         :return:
#         """
#         if not self.graph:
#             return
#
#         flag = False
#         for i in range(self.max_iterations):
#             change = 0.0  # 记录每轮的变化值
#             norm = 0  # 标准化系数
#             tmp = {}
#             # 计算每个页面的authority值
#             tmp = self.authority.copy()
#             for node in self.graph.nodes():
#                 self.authority[node] = 0
#                 for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
#                     self.authority[node] += self.hub[incident_page]
#                 norm += pow(self.authority[node], 2)
#             # 标准化
#             norm = sqrt(norm)
#             for node in self.graph.nodes():
#                 self.authority[node] /= norm
#                 change += abs(tmp[node] - self.authority[node])
#
#             # 计算每个页面的hub值
#             norm = 0
#             tmp = self.hub.copy()
#             for node in self.graph.nodes():
#                 self.hub[node] = 0
#                 for neighbor_page in self.graph.neighbors(node):  # 遍历所有“出射”的页面
#                     self.hub[node] += self.authority[neighbor_page]
#                 norm += pow(self.hub[node], 2)
#             # 标准化
#             norm = sqrt(norm)
#             for node in self.graph.nodes():
#                 self.hub[node] /= norm
#                 change += abs(tmp[node] - self.hub[node])
#
#
#
#             if change < self.min_delta:
#                 flag = True
#                 # break
#                 print("This is NO.%s iteration" % (i + 1))
#                 authority=self.authority
#                 hub=self.hub
#                 print("authority", self.authority)
#                 print("hub", self.hub)
#                 break
#
#         if flag:
#             print("finished in %s iterations!" % (i + 1))
#         else:
#             print("finished out of 100 iterations!")
#
#         print("The best authority page: ", max(self.authority.items(), key=lambda x: x[1]))
#         print("The best hub page: ", max(self.hub.items(), key=lambda x: x[1]))
#         return authority.items(),hub.items()

# dg = digraph()
#
# with open('/app/static/csv/names_message.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#     for row in reader:
#         dg.add_nodes([row[0]])
#
# with open('/app/static/csv/relation_message.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#     for row in reader:
#         dg.add_edge((str(row[1]), str(row[2])))
# hits = HITSIterator(dg)
# hits.hits()

#pagerank算法
from pygraph.classes.digraph import digraph

#
# class PRIterator:
#     __doc__ = '''计算一张图中的PR值'''
#
#     def __init__(self, dg):
#         self.damping_factor = 0.85  # 阻尼系数,即α
#         self.max_iterations = 100  # 最大迭代次数
#         self.min_delta = 0.00001  # 确定迭代是否结束的参数,即ϵ
#         self.graph = dg
#
#     def page_rank(self):
#         #  先将图中没有出链的节点改为对所有节点都有出链
#         for node in self.graph.nodes():
#             if len(self.graph.neighbors(node)) == 0:
#                 for node2 in self.graph.nodes():
#                     digraph.add_edge(self.graph, (node, node2))
#
#         nodes = self.graph.nodes()
#         graph_size = len(nodes)
#
#         if graph_size == 0:
#             return {}
#         page_rank = dict.fromkeys(nodes, 1.0 / graph_size)  # 给每个节点赋予初始的PR值
#         damping_value = (1.0 - self.damping_factor) / graph_size  # 公式中的(1−α)/N部分
#
#         flag = False
#         for i in range(self.max_iterations):
#             change = 0
#             for node in nodes:
#                 rank = 0
#                 for incident_page in self.graph.incidents(node):  # 遍历所有“入射”的页面
#                     rank += self.damping_factor * (page_rank[incident_page] / len(self.graph.neighbors(incident_page)))
#                 rank += damping_value
#                 change += abs(page_rank[node] - rank)  # 绝对值
#                 page_rank[node] = rank
#
#
#             if change < self.min_delta:
#                 flag = True
#                 break
#         if flag:
#             print("finished in %s iterations!" % node)
#         else:
#             print("finished out of 100 iterations!")
#         return page_rank
#
# dg = digraph()
#
# with open('/app/static/csv/names_message.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#     for row in reader:
#         dg.add_nodes([row[0]])
#
#     print(dg)
# with open('/app/static/csv/relation_message.csv', 'r') as f:
#     reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#     for row in reader:
#         dg.add_edge((str(row[1]), str(row[2])))
# pr = PRIterator(dg)
# page_ranks = pr.page_rank()
#
# print("The final page rank is\n", page_ranks)






def spider(name):
    #全部名字的列表
    node=[]
    nodeslist=[]
    #列表字典
    node_all=[]
    edge_all = []
    node_res=[]
    edge_res=[]
    a=[]
    n=[]
    n.append(name)

    with open('../static/csv/names_message.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
        for i in reader:
            node.append(i[0])
            node_all.append({'name':i[0]})

    with open('../static/csv/relation_message.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
        for i in reader:
            edge_all.append({'source': node.index(i[1]), 'target': node.index(i[2]), 'relation': i[3]})
            if i[1]==name or name==i[2]:
                n.append(i[1])
                n.append(i[2])
                a.append((i[1],i[2],i[3]))

    n=list(set(n))
    for i in n:
        node_res.append({'name':i})
    for j in a:
        edge_res.append({'source':n.index(j[0]),'target':n.index(j[1]),'relation':j[2]})




    if name =="all":
        return node_all,edge_all
    else:
        return node_res,edge_res


# 度分布图生成
# def degeree():
#     degree1=[]
#     with open('/app/static/csv/relation_message.csv', 'r') as f:
#         reader = csv.reader(f, delimiter=',')
#         for row in reader:
#             degree1.append(row[1])
#             degree1.append(row[2])
#
#     tf= {}
#     for i in degree1:
#         if i in tf:
#             tf[i] += 1
#         else:
#             tf[i] = 1
#
#     lst=list(tf.values())
#
#     dic={}
#     for i in lst:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i] = 1
#
#     x=list(dic.keys())
#     x.sort()
#
#     y=list(dic.values())
#     x=np.array(x)
#     y=np.array(y)
#     x_smooth=np.linspace(x.min(),x.max(),300)
#     y_smooth=make_interp_spline(x,y)(x_smooth)
#     plt.plot(x_smooth,y_smooth)
#     plt.savefig("./static/dufenbu.png")


#度中心性
# def center():
#     y=np.zeros([182,182],dtype=int)
#     nodeslist=[]
#     with open('/app/static/csv/names_message.csv', 'r') as f:
#         reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#         for row in reader:
#             nodeslist.append(row[0])
#
#
#     with open('/app/static/csv/relation_message.csv', 'r') as f:
#         reader = csv.reader(f, delimiter=',')  # 默认的情况下, 读和写使用逗号做分隔符(delimiter)
#         for row in reader:
#             y[nodeslist.index(str(row[1]))][nodeslist.index(str(row[2]))]=1
#
#     np.savetxt(r'test1.txt', y,fmt='%d', delimiter=',')




# def matrix_to_graph():
#     G = nx.Graph()
#     matrix=y
#     nodes = range(len(matrix))
#     G.add_nodes_from(nodes)
#
#     for i in range(len(matrix)):
#         for j in range(len(matrix)):
#             if (matrix[i][j] == 1):
#                 G.add_edge(i, j)
#
#     dc = nx.algorithms.centrality.degree_centrality(G)
#
#
#     # 将字典的形式转化成按照value从小到大排序
#     list_dc = sorted(dc.items(), key=operator.itemgetter(1),reverse = True)
#
#     lst1=[]
#     for i in range(11):
#         lst1.append(list_dc[i])
#
#     return lst1
#
#
# matrix_to_graph()
lstt = [0, 17, 3, 6, 41, 54, 113, 1, 2,115]
