import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import os

def cloud(text, title, label=1):
    if(label==1):
        wordcloud = WordCloud(width=1000, height=500, background_color='white', max_words=1000,
                              colormap='plasma').generate(text)
        plt.imshow(wordcloud)
        plt.axis("off")
        plt.title(title)
        name = title.split('@')[0]
        filename = "wordcloud/" + name + '/'+ title + ".jpg"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        plt.savefig(filename)
    else:
        wordcloud = WordCloud(width=1000, height=500, max_words=1000).generate(text)
        plt.imshow(wordcloud)
        plt.title(title)
        name = title.split('@')[0]
        filename = "wordcloud/" + name + '/' + title + ".jpg"
        dirname = os.path.dirname(filename)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        plt.savefig(filename)


df = pd.read_csv('processed.csv', engine='python')
name = df['name']
date = df['date']
review = df['review']
neg_list = []
neu_list = []
pos_list = []

for i in range(len(review)):
    text = review[i]
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(text)
    neg_list.append(ss['neg'])
    neu_list.append(ss['neu'])
    pos_list.append(ss['pos'])
    if(ss['neg']<ss['pos']):
        cloud(text, name[i]+'@'+date[i]+"@positive", label=1)
    else:
        cloud(text, name[i]+'@'+date[i]+"@negative", label=2)


data = {'name': df['name'],
        'address': df['address'],
        'date': df['date'],
        'neg':pd.Series(neg_list),
        'neu':pd.Series(neu_list),
        'pos':pd.Series(pos_list),
        }
dataMat = pd.DataFrame(data)
dataMat.to_csv('dataMat.csv')
