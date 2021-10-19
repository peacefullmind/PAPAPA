import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlwt

ll=[]
chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
url='https://twitter.com/fuchsiadunlop'
driver.get(url)

time.sleep(5)


for i in range(85):
    print('===========================================')
    print("i={}".format(i))
    html=driver.page_source
    soup=bs(html, 'html.parser')
    divs=soup.find_all("div", class_="css-901oao r-18jsvk2 r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0")
    for div in divs:
        span=div.find("span",class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
        try:
            print(span.text)
            ll.append(span.text)
        except:
            print("未获取到此条数据")


    #'span',
    # spans=soup.find_all("span",class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")
    #
    # for span in spans:
    #     # print(span.text)
    #     ll.append(span.text)

    print('获取一页')
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)




#===================================================================================================
ll=list(set(ll))
print(ll)

workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('推文')
# 写入excel
# 参数对应 行, 列, 值
i = 1
for l in ll:
    worksheet.write(i, 0, label=l)
    i = i + 1
# 保存
workbook.save('推文2.xls')
