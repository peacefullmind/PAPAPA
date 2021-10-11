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
    flag_exe=1

    while(flag_exe):
        # 点击more
        try:
            driver.execute_script('document.getElementsByClassName("taLnk ulBlueLinks")[0].click()')
            print('点击more')
            time.sleep(5)
        except:
            pass

        html = driver.page_source
        soup = bs(html, 'html.parser')
        ps = soup.find_all('p', {'class': 'partial_entry'})

        for p in ps:
            p=p.text
            remark.append(p)

         #判断是否是最后一页，如果是最后一页，择flag置0，若不是最后一页，则翻页
        try:
            driver.execute_script('document.getElementsByClassName("nav next ui_button primary")[0].click()')
            print('翻页')
            time.sleep(5)
        except:
            print("找不到下一页")
            flag_exe=0
        try:
            driver.execute_script('document.getElementsByClassName("nav next ui_button primary disabled")[0].click()')
            print('已到达最后一页')
            flag_exe=0
        except:
            pass




    print('获取到{}条评论'.format(len(remark)))
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


global k
#===================================
k=1

global name
name='Thai'

data = xlrd.open_workbook("数据{}.xls".format(name))
table = data.sheet_by_name("My Worksheet")
urls=table.col_values(0, start_rowx=k, end_rowx=None)#返回由该列中所有单元格的数据组成的列表


for url in urls:
    create_table(url)
    k=k+1

