import numpy as np
import pandas as pd
import calplot
import matplotlib as mpl
import matplotlib.pylab as plt
from matplotlib.colors import LinearSegmentedColormap


# 读取表格
# localId TalkerId Type SubType IsSender CreateTime StrContent StrTime Count
path = "data.xlsx"
df = pd.read_excel(path,usecols=['localId','StrTime'])

# 将时间列转化为时间类型
df['StrTime'] = pd.to_datetime(df['StrTime'])

# 设置索引
df.set_index('StrTime', inplace=True)

# 按天统计聊天数
df_day = df.resample('d').count()
df_day = df_day[df_day['localId'] != 0]
print(df_day)


# 绘制日历热力图
colors = ["#F6E1E8", "#F00859"]
my_cmap = LinearSegmentedColormap.from_list('my_cmap',colors, N=256)
mpl.colormaps.register(cmap=my_cmap)

pl1 = calplot.calplot(data=df_day['localId'], 
                      how='sum', 
                      cmap='my_cmap', 
                      edgecolor=None, 
                      textformat ='{:.0f}', 
                      dropzero = True,
                      colorbar = False,
                      textcolor = 'k')
plt.show()
