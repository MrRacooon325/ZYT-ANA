import numpy as np
import pandas as pd
from PIL import Image
import matplotlib.pyplot as plt
import jieba
import  wordcloud
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap


#读取自定义词典
jieba.load_userdict(r"dictionary.txt")

#读取文本
file=open(r"data.txt",encoding ="utf-8")
text=file.read()
file.close()

#设置中文显示
plt.rcParams['font.sans-serif']=['SimHei']

#分词处理
wordlist = list(jieba.cut(text))
wordlist = [word for word in wordlist if len(word)>1]
wordlist = [word for word in wordlist if not word.isdecimal()]

#连接分出的单词
word = " ".join(wordlist)

#读取停用词
stopfile = open(r"stopwords.txt",encoding ="utf-8")
stopwords = stopfile.read().split("\n")
stopfile.close


# # 词频统计
# counts = {} # 新建立一个空的字典
# for i in wordlist: # 循环遍历所有的单词
#     if i not in stopwords:
#         counts[i] = counts.get(i,0)+1 # 返回word这个键对应的值，只要是出现的单词都默认值为 1，下次如果再遇到就加一
# items = list(counts.items()) # 将字典中的值都放入列表中，这个时候应该是一个元组类型的列表

# #对列表大到小排序
# items.sort(key=lambda x:x[1],reverse=True) # lambda关键字表示按照后面指定的方式进行排序，这里表示元组中的第二个元素，也就是单词出现的次数
# for i in range(40): # 循环的打印出出现频率最高的前20个单词
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))
# # print(items)
    

# 词云处理

colors = ["#D0C7CA", "#F00859"]
my_cmap = LinearSegmentedColormap.from_list('my_cmap',colors, N=256)
mpl.colormaps.register(cmap=my_cmap)

# imgpath=np.array(Image.open( r"xxx.png"))#定义下词云背景图片路径
wc = wordcloud.WordCloud( font_path='C:\Windows\Fonts\SIMKAI.TTF',
                          background_color='white',
                          mask=None,
                          max_words=200,
                          max_font_size=150,
                          width=900,
                          height=900,
                          scale=17,
                          random_state=None,
                          stopwords=stopwords,
                          collocations=False,
                          colormap='my_cmap',
                          prefer_horizontal=0.8)

wc.generate(word) #传入需画词云图的文本

#对词云进行展示
plt.imshow(wc)

plt.axis("off")# 隐藏图像坐标轴
# plt.savefig(r"bar_img.png", dpi=400)#保存图片
plt.show()# 展示图片


