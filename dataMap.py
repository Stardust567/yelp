import pandas as pd
from geopy.geocoders import Nominatim

# 生成最新的地图经纬度数据

df = pd.read_csv('data/dataMat.csv', engine='python')
df.drop_duplicates('address', keep='first', inplace=True)
address = df['address'].str.split(',', 1).str[0]
latitude = []
longitude = []
name = []
neg = []
pos = []

for i in range(len(address)):
    geolocator = Nominatim(timeout=3000)
    location = geolocator.geocode(address.iloc[i])
    if location is None:
        print('*****************')
    else:
        print(location.latitude, location.longitude)
        latitude.append(location.latitude)
        longitude.append(location.longitude)
        name.append(df['name'].iloc[i])
        neg.append(df['neg'].iloc[i])
        pos.append(df['pos'].iloc[i])

data = {'name': pd.Series(name),
        'latitude': pd.Series(latitude),
        'longitude': pd.Series(longitude),
        'neg':pd.Series(neg),
        'pos':pd.Series(pos),
        }

dataMap = pd.DataFrame(data)
'''
list = dataMap[(dataMap.latitude == 1)].index.tolist()
dataMap = dataMap.drop(list)
list = dataMap[(dataMap.longitude == 1)].index.tolist()
dataMap = dataMap.drop(list)

dataMap['name'] = dataMap['name'].fillna('hhh')
list = dataMap[(dataMap.name == 'hhh')].index.tolist()
dataMap = dataMap.drop(list)
'''
dataMap.to_csv('data/dataMap.csv')