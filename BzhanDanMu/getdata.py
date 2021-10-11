import requests
import re

for page in range(20,30):
    url=f'https://api.bilibili.com/x/v2/dm/web/history/seg.so?type=1&oid=284687902&date=2021-03-{page}'
    headers={
    'cookie':'LIVE_BUVID=AUTO4716193553517960; _uuid=AEAB90FE-456A-4FB5-BEC8-69C2B74B667E52982infoc; buvid3=31DE5ECC-1497-41F2-8933-D0626320EF5434771infoc; CURRENT_FNVAL=80; blackside_state=1; bsource=search_baidu; rpdid=|(J~kkRk)RJu0J\'uYum~|mm~J; PVID=1; bfe_id=603589b7ce5e180726bfa88808aa8947; fingerprint=d4ca67690252b0e2e428a4bacb44b7bf; buvid_fp=31DE5ECC-1497-41F2-8933-D0626320EF5434771infoc; buvid_fp_plain=31DE5ECC-1497-41F2-8933-D0626320EF5434771infoc; SESSDATA=57c12b9d%2C1635262587%2C13174%2A41; bili_jct=b9c6db92a60c60384afd233e1843fb21; DedeUserID=249993932; DedeUserID__ckMd5=c28e74acb2161e40; sid=4mmt05r9',
    'origin': 'https://www.bilibili.com',
    'referer': 'https://www.bilibili.com/video/BV1QX4y1K7DX?from=search&seid=12750593819563835576',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'

    }
    response=requests.get(url=url,headers=headers)
    # print(response.text)
    data=re.findall('.*?([\u4e00-\u9fa5]+).*',response.text)
    # print(data)
    for da in data:
        print(da)
        # a是追加，w的话只会有最后一个，不换行的话会写在一行
        with open("弹幕.txt",mode='a',encoding='utf-8') as f:
            f.write(da)
            f.write('\n')
