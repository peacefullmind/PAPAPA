import requests
import json

url='https://chongqing.anjuke.com/esf-ajax/property/info/pc/area/business/?city_id=20&page_size=10&area_id=2359&from=sale_map&page=1&select_type=0'
header={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36','referer': 'https://chongqing.anjuke.com/sale/yubei/?from=sale_map'}
mycookie={'cookie':'sessid=FA5DADAA-F544-92CD-A106-A505D73579B3; aQQ_ajkguid=5EB6A80A-859A-16C5-39D8-323C1810F941; id58=e87rkF/chwKQr/OBBT+KAg==; _ga=GA1.2.1522895678.1608288003; 58tj_uuid=f6cdd636-2fbf-4763-9760-b1e34553d784; als=0; xxzl_cid=5dfe5c053c18490d9b04b8276a974eb3; xzuid=1135c1b7-88af-4876-8383-a8384eb80dc0; ctid=20; twe=2; _gid=GA1.2.25214172.1611587986; new_uv=2; obtain_by=2'}
res=requests.get(url=url,headers=header,cookies=mycookie)

url2='https://chongqing.anjuke.com/sale/yubei/?from=sale_map#'
res2=requests.get(url=url2,headers=header,cookies=mycookie)
# print(res2.json())
myhtml=res2.text
print(myhtml)


