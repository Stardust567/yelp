import pandas as pd

def dataProcess(send_url, recv_url):
    df = pd.read_csv(send_url, engine='python')

    df['name'] = df['name'].fillna('hhh')
    list = df[(df.name == 'hhh')].index.tolist()
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

    df['review'] = df['review'].str.replace("[^a-zA-Z#]", " ")
    print(df.info())
    df.to_csv(recv_url)