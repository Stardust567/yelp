import pandas as pd
from matplotlib import pyplot as plt
import os


def get_linePicture(title, time, key1, value1, color_set=0, key2='', value2=[], split=False, bar=True,
                    save=False):
    '''
    绘制折线图
    :param title: 股票名
    :param time: 时间序列
    :param key1: 第一个指标名
    :param value1: 第一个指标的数据
    :param key2: 第二个指标名（默认为空格' '）
    :param value2: 第二个指标的数据（默认为空集[])
    :param split: 是否设置左右两个y轴（默认为否False）
    :param save: 是否存图（默认False）
    '''
    fig, ax1 = plt.subplots(facecolor='#FFF7E3')
    date = time
    time = range(len(date))
    color = ['tab:blue', 'tab:orange',
             'tab:green', 'tab:red',
             'tab:purple', 'tab:brown',
             'tab:pink', 'tab:gray',
             'tab:olive', 'tab:cyan']
    # blue, orange, green, red, purple, brown, pink, gray, olive, cyan
    plt.xticks(time, date, rotation=30)
    ax1.tick_params(axis='x', labelcolor=color[7])
    ax1.set_ylabel(key1)
    ax1.tick_params(axis='y', labelcolor=color[color_set])
    ax1.plot(time, value1, '--', color=color[color_set], marker='*', label=key1)
    plt.title(title)
    ax1.grid(True)
    if (bar is True):
        ax1.bar(time, value1, align="center", width=0.5, alpha=0.5, color=color[color_set])

    if (len(value2) != 0):
        if (split is False):
            ax1.plot(time, value2, '-.', color=color[1], marker='*', label=key2)
            ax1.tick_params(axis='y', labelcolor=color[1])
            ax1.legend(loc=2)
            if (bar is True):
                ax1.bar(time, value2, align="edge", width=0.5, alpha=0.5, color=color[1])

        if (split is True):
            ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
            ax2.set_ylabel(key2)
            ax2.tick_params(axis='y', labelcolor=color[1])
            ax2.plot(time, value2, '-.', color=color[1], marker='*', label=key2)
            ax2.grid(False)
            if (bar is True):
                ax2.bar(time, value2, align="edge", width=0.5, alpha=0.5, color=color[1])

        fig.tight_layout()  # otherwise the right y-label is slightly clipped

    if (save is True):
        filename ='linePicture/' + title + ".png"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        fig.savefig(filename)

    plt.close('all')

df = pd.read_csv('data/dataMat.csv', engine='python')
name = df['name']
names = list(set(list(name)))
for name in names:
    temp = df[df['name']==name]
    pos = temp['pos']
    neg = temp['neg']
    date = temp['date']
    get_linePicture(name, date, 'pos', pos, color_set=0, key2='neg', value2=neg, split=False, bar=True,
                    save=True)
