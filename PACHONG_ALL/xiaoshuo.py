import requests
import parsel

def download_one_chapter(url):
    # 先爬取一章
    # 请求网页，获取数据
    response = requests.get(url)
    response.encoding = response.apparent_encoding
    # print(response.text)
    sel = parsel.Selector(response.text)
    title = sel.css('h1::text')
    contect = sel.css('#content::text')
    #print(title.get())
    lines = contect.getall()
    mytext = ''
    for line in lines:
        mytext += line.strip() + '\n'

    #print(mytext)
    mtemp: str=str(title.get())
    #mtemp2=mtemp+'.txt'
    #print(mtemp2)
    with open(file='./output/' + mtemp + '.txt', mode='w', encoding='utf -8') as f:
        f.write(mtemp)
        f.write(mytext)

#download_one_chapter('http://www.shuquge.com/txt/63542/31289840.html')
#download_one_chapter('http://www.shuquge.com/txt/63542/31289840.html')

response=requests.get('http://www.shuquge.com/txt/63542/index.html')
sel = parsel.Selector(response.text)
urls=sel.css('dd > a::attr(href)').getall()

for url in urls:
    #print('http://www.shuquge.com/txt/63542/'+url)
    download_one_chapter('http://www.shuquge.com/txt/63542/'+url)
