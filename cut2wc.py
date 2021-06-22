from wordcloud import WordCloud
import jieba
import matplotlib.pyplot as plt
import time


def cutwords(words):
    # print(txt)
    jieba.load_userdict("AIDict.txt")
    seg_list = jieba.cut(words, cut_all=False)

    tf = {}
    for seg in seg_list:
        if seg in tf:
            tf[seg] += 1
        else:
            tf[seg] = 1

    ci = list(tf.keys())
    with open('stopword.txt', 'r') as ft:
        stopword = ft.read()
    for seg in ci:
        if tf[seg] < 10 or len(seg) < 2 or seg in stopword or '一' in seg:
            tf.pop(seg)
    # print(len(tf))

    ci = list(tf.keys())
    num = list(tf.values())
    data = []

    for i in range(len(tf)):
        data.append((num[i], ci[i]))

    data.sort()
    data.reverse()
    return data


# def w_cloud(data):
#     wcdata = {}
#     for d in data:
#         wcdata[d[1]] = d[0]
#     # print(wcdata)
#     font = r'/Users/fairy/PycharmProjects/爬虫4/娃娃体/Wawati SC/WawaSC-Regular.otf'
#     wc = WordCloud(font_path=font, background_color='white').generate_from_frequencies(wcdata)
#
#     # plt.imshow(wc)
#     # plt.axis('off')
#     # plt.show()
#     datetime = time.strftime("%Y%m%d%H%M%S",time.localtime())
#     name = "app/static/img"+datetime+".jpg"
#     wc.to_file(name)
#     return name


#
# if __name__ == '__main__':
#     xnxi = [(291, '中国'), (268, '发展'), (202, '建设'), (197, '学校'), (193, '教育'), (188, '工作'), (140, '传媒大学'), (134, '学习'),
#             (113, '书记'), ]
#     w_cloud(xnxi)
