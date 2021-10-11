import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import time
import xlwt,xlrd

def create_table(url):
    remark=[]
    # url='https://www.tripadvisor.com/Restaurant_Review-g297463-d15278567-Reviews-Lobby_Lounge-Chengdu_Sichuan.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}
    chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chromeDriver)
    driver.get(url=url)
    driver.maximize_window()
    time.sleep(5)
    # 点击more



    try:
        driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[6]/div/div[1]/div[4]/div/div[5]/div/div[1]/div[2]/div/div/div/div[2]/div[2]/div/p/span[2]').click()
        time.sleep(8)
    except:
        pass

    try:
        driver.find_element_by_xpath('//*[@id="review_805754679"]/div/div[2]/div[3]/div/p/span')
        time.sleep(2)
    except:
        pass

    html=driver.page_source
    # html=requests.get(url=url,headers=headers).text
    soup=bs(html,'html.parser')
    divs = soup.find_all('div', {'class': 'mobile-more'})
    for div in divs:
        try:
            ptext=div.find('p',{'class':'partial_entry'}).text
            remark.append(ptext)
        except:
            ptext=''


    print(remark)


    workbook = xlwt.Workbook(encoding='utf-8')
    # 创建一个worksheet
    worksheet = workbook.add_sheet('评论')
    # 写入excel
    # 参数对应 行, 列, 值
    i = 1
    for l in remark:
        worksheet.write(i, 0, label=url)
        worksheet.write(i, 1, label=l)
        i = i + 1
    # 保存
    workbook.save('./评论/评论{}.xls'.format(k))
    driver.close()


data = xlrd.open_workbook("数据.xls")
table = data.sheet_by_name("My Worksheet")
urls=table.col_values(0, start_rowx=1, end_rowx=None)#返回由该列中所有单元格的数据组成的列表

global k
k=1
for url in urls:
    create_table(url)
    k=k+1

