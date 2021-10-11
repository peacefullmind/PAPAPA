import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlwt


def get_url(driver):
    print('进入函数')
    html = driver.page_source
    # print(html)
    soup = bs(html, "html.parser")  # page_source得到当前网页的源代码
    #
    divs = soup.find_all('div', {'class': 'cauvp Gi o'})
    print(divs)
    for div in divs:
        t = div.find('div', {'class': 'OhCyu'})
        link = t.find('a').get('href')
        # print(link)
        # print('===================================')
        my_link = base_url + link
        link_list.append(my_link)


# url = 'https://www.tripadvisor.com/Restaurants-g297463-Chengdu_Sichuan.html'
# url='https://www.tripadvisor.com/Restaurants-g608466-Mianyang_Sichuan.html'
# url='https://www.tripadvisor.com/Restaurants-g303771-Leshan_Sichuan.html'
# url='https://www.tripadvisor.com/Restaurants-g658403-Zigong_Sichuan.html'
# url='https://www.tripadvisor.com/Restaurants-g635746-Deyang_Sichuan.html'
chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
base_url = 'https://www.tripadvisor.com'

global link_list
link_list = []

url='https://www.tripadvisor.com/Restaurants-g297463-Chengdu_Sichuan.html'
driver.get(url=url)
time.sleep(5)
# 点击 show more
# driver.find_element_by_xpath('//*[@id="component_48"]/div/div[5]/div[2]/div[5]').click()

global name
name='Thai'

# 页面
page=1

#手动点击Italian
print('手动点击{}'.format(name))
# 手动点击szchuan
time.sleep(60)


get_url(driver=driver)
print('获取一页url')
driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
time.sleep(5)


# for i in range(page-1):
#     print(i)
#     get_url(driver=driver)
#     print('获取一页url')
#     driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(5)
#     print('拉到最后')
#     if i == 0:
#         xpath = '//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a'
#     else:
#         xpath = '//*[@id="EATERY_LIST_CONTENTS"]/div[2]/div/a[2]'
#
#     driver.find_element_by_xpath(xpath).click()
#     time.sleep(5)
print('============最后结果================')
print(link_list)

workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')
# 写入excel
# 参数对应 行, 列, 值
i = 1
for l in link_list:
    worksheet.write(i, 0, label=l)
    i = i + 1
# 保存
workbook.save('数据{}.xls'.format(name))
