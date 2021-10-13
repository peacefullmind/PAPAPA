import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import xlwt

chromeDriver = "D:\\chromedriver_win32\\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chromeDriver)
url='https://twitter.com/fuchsiadunlop'
driver.get(url)

time.sleep(40)

html=driver.page_source
soup=bs(html, 'html.parser')

#'span',
spans=soup.find_all("span",class_="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0")

for span in spans:
    print(span.text)

