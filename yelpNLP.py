import pandas as pd
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import os

def cloud(text, title):

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
    print(filename)

df = pd.read_csv('data/processed.csv', engine='python')
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
    cloud(text, name[i]+'@'+date[i])


data = {'name': df['name'],
        'address': df['address'],
        'date': df['date'],
        'neg':pd.Series(neg_list),
        'neu':pd.Series(neu_list),
        'pos':pd.Series(pos_list),
        }
dataMat = pd.DataFrame(data)
dataMat.to_csv('data/dataMat.csv')
