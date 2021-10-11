from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs


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
    print(remark)

url='https://www.tripadvisor.com/Restaurant_Review-g608466-d3426041-Reviews-SiHai_Xiang-Mianyang_Sichuan.html'
create_table(url)
