from pyecharts import options as opts
from pyecharts.charts import Map
import  requests
import json

myurl="https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
respoonse=requests.get(myurl)

myrawjson=respoonse.json()
mydata=json.loads(myrawjson['data'])["areaTree"][0]["children"]


new_data={}

for i in mydata:
    new_data[i['name']]=i['total']['confirm']

name=new_data.keys()
num=new_data.values()
print(zip(name,num))
for i in zip(name,num):
    print(list(i))

def new_maps():
    myMap=Map()
    myMap.add(
        '疫情地图',
        [list(i) for i in zip(new_data.keys(), new_data.values())],
        'China',
        is_map_symbol_show=False

    )
    myMap.set_global_opts(
        title_opts=opts.TitleOpts(
            title="sss"
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True
        )
    )
    myMap.render('fs.html')
new_maps()


