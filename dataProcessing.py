import pandas as pd

def dataProcess(send_url, recv_url):
    '''
    进行最初始的数据清洗
    :param send_url: 清洗的原文件
    :param recv_url: 导出的文件名
    :return:
    '''
    df = pd.read_csv(send_url, engine='python')

    df['name'] = df['name'].fillna('hhh')
    list = df[(df.name == 'hhh')].index.tolist()
    df = df.drop(list)
    for name in df['name']:
        if (((df[df['name'] == name]).count()).values[0] < 5):
            list = df[(df.name == name)].index.tolist()
            df = df.drop(list)

    df['address'] = df['address'].fillna('hhh')
    list = df[(df.address == 'hhh')].index.tolist()
    df = df.drop(list)

    df['date'] = df['date'].fillna('hhh')
    list = df[(df.date == 'hhh')].index.tolist()
    df = df.drop(list)

    df['review'] = df['review'].fillna('hhh')
    list = df[(df.review == 'hhh')].index.tolist()
    df = df.drop(list)

    df['date'] = df['date'].str.replace("\n", "")
    df['date'] = df['date'].str.replace("/", "_")
    df['date'] = df['date'].str.replace(" ", "")
    df['address'] = df['address'].str.replace("\n", "")
    df['review'] = df['review'].str.replace("[^a-zA-Z#]", " ")
    df['name'] = df['name'].str.replace("[^a-zA-Z#]", "")
    print(df.info())
    df.to_csv(recv_url)

dataProcess('test.csv', 'data/processed.csv')