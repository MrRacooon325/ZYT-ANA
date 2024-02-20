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

# 获取特定时间段数据
df = df['2023-10':'2023-12']


# 按日统计聊天数
df_month = df.resample('d').count()

pydate_array = df_month.index.to_pydatetime()
date_only_array = np.vectorize(lambda s: s.strftime('%m月%d日'))(pydate_array)
df_month['time'] = date_only_array


#设置中文显示
plt.rcParams['font.sans-serif']=['SimHei']

#绘制折现图
plt.plot(df_month.time,
        df_month.localId,
        color='#E61F59')


#绘制网格
plt.grid(axis="y",
         linestyle='-.')

# plt.tight_layout()

plt.xticks(rotation = 90)


plt.show()
