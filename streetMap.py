import osmapi
import pandas as pd
import folium
import webbrowser
import json
import os

dataMat = pd.read_csv('data/dataMap.csv', engine='python')
x = dataMat['latitude']
y = dataMat['longitude']
name = dataMat['name']

m = folium.Map(
        location=[30.3, -97.7],
        zoom_start=7,
        tiles='Stamen Terrain'  # 更改了展开图样式
    )

for i in range(len(name)):
    temp = []
    temp.append(dataMat['name'].iloc[i])
    temp.append(dataMat['pos'].iloc[i])
    temp.append(dataMat['neg'].iloc[i])
    list = []
    list.append(temp)
    print(list)
    df = pd.DataFrame(data=list, columns=['name', 'pos', 'neg'])
    html = df.to_html()

    lng = x.iloc[i]
    lat = y.iloc[i]
    folium.Marker(location=[lng,lat], popup=folium.Popup(html,max_width=450)).add_to(m)


file_path = r"yelpAustin.html"
m.save(file_path)

webbrowser.open(file_path)
'''
api = osmapi.OsmApi(api="https://api06.dev.openstreetmap.org", username = "Stardust567", password = "openstreetmap")
api.ChangesetCreate({u"comment": u"yelpReview"})
for i in range(len(x)):
    print(api.NodeCreate({u"lon": y[i], u"lat": x[i], u"tag": {'name': name[i]}}))
api.ChangesetClose()
'''