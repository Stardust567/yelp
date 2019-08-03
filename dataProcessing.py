import pandas as pd
df = pd.read_csv('test.csv', engine='python')
'''
df = pd.read_csv('test.csv', engine='python')
word = df.ix[877]
print(word)
print(word['address'])
print(word['name'])
print(type(word['address']))
if(type(word['address'])==type(1.1)):
    print('*********************************')
print(word['date'])
#print(word['review'])

for i in range(1659):
    word = df.ix[i]
    word['name'] = word['name'].strip('\n')
    if (type(word['address']) == type(1.1)):
        temp = df.ix[i-1]
        word['address'] = temp['address']
    else:
        word['address'] = word['address'].strip('\n')
        word['address'] = (word['address'].split(','))[0]
    word['date'] = word['date'].strip('\n')
    word['review'] = word['review'].strip('\n')
df.to_csv('test.csv')
'''
df['name'] = df['name'].fillna('hhh')
list = df[(df.name=='hhh')].index.tolist()
print(list)
df = df.drop(list)
df['address'] = df['address'].fillna('hhh')
list = df[(df.address=='hhh')].index.tolist()
df = df.drop(list)
df['date'] = df['date'].fillna('hhh')
list = df[(df.date=='hhh')].index.tolist()
df = df.drop(list)
df['review'] = df['review'].fillna('hhh')
list = df[(df.review=='hhh')].index.tolist()
df = df.drop(list)
print(df.info())
df.to_csv('process.csv')