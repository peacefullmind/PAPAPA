import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlwt

chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
url='https://twitter.com/fuchsiadunlop'
driver.get(url)
