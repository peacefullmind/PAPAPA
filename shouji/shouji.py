import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time

url='https://eblife.ebchinatech.com/eblifeSpread/?channelCode=1814000000&introduction=18000415#/download?channel=1800000000&introduction=18000415'
headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    }
r = requests.get(url, headers=headers)

bs = BeautifulSoup(r.text, "html.parser")
print(r.text)
print(r.status_code)

# #打开网址
# chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"
# # driver = webdriver.Chrome(executable_path=chromeDriver)
#
# # 进入浏览器设置
# options = webdriver.ChromeOptions()
#
# # 设置中文
# options.add_argument('lang=zh_CN.UTF-8')
#
# # 修改User Agent
# options.add_argument('user-agent="Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"')
#
#
# driver = webdriver.Chrome(chrome_options=options,executable_path=chromeDriver)
# driver.get(url=url)
# time.sleep(1)  # 休眠2秒
# driver.find_element_by_xpath('//*[@id="downloadButton"]').click()