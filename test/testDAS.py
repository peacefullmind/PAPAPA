
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from bs4 import BeautifulSoup as bs
import xlwt

from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)

# 打开网址
# driver.set_window_size(800,600)
url = 'http://25.1.0.207:8080/DAS/index.go?reqCode=indexInit'
driver.get(url=url)
time.sleep(1)  # 休眠2秒

driver.find_element_by_xpath('//*[@id="account"]').clear()
driver.find_element_by_xpath('//*[@id="account"]').send_keys('18000415')
driver.find_element_by_xpath('//*[@id="password"]').clear()
driver.find_element_by_xpath('//*[@id="password"]').send_keys('Abcde@123')
driver.find_element_by_xpath('//*[@id="ext-gen28"]').click()
time.sleep(1)  # 休眠2秒

# 点击期间管理
driver.find_element_by_xpath('//*[@id="ext-gen26"]/div/li[5]/div/a/span').click()
time.sleep(1)  # 休眠2秒

# print('=============================================')
# print('请选择期间')
# print('=============================================')
# time.sleep(3)
#处理下拉框
driver.


#点击查询
driver.find_element_by_id('ext-gen64').click()
time.sleep(1)  # 休眠2秒

data=driver.find_element_by_xpath('//*[@id="ext-gen27"]/div/table').text
print(data)
