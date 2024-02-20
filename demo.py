import numpy as np
import pandas as pd
import calplot
import matplotlib as mpl
import matplotlib.pylab as plt
from matplotlib.colors import ListedColormap,LinearSegmentedColormap


# 读取表格
# localId TalkerId Type SubType IsSender CreateTime StrContent StrTime Count
path = "data.xlsx"
df = pd.read_excel(path,usecols=['localId','StrTime'])

# 将时间列转化为时间类型
df['StrTime'] = pd.to_datetime(df['StrTime'])

# 设置索引
df.set_index('StrTime', inplace=True)


# 按月统计聊天数
df_month = df.resample('m').count()

pydate_array = df_month.index.to_pydatetime()
date_only_array = np.vectorize(lambda s: s.strftime('%Y年%m月'))(pydate_array)
df_month['time'] = date_only_array


#设置中文显示
plt.rcParams['font.sans-serif']=['SimHei']

#绘制柱状图
plt.bar(x=df_month.time,
        height=df_month.localId,
        color='#E61F59')


#绘制网格
plt.grid(axis="y",
         linestyle='-.')

# plt.tight_layout()

plt.xticks(rotation = 90)


plt.show()
#xx