from selenium import webdriver

driver=webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
driver.get('https://www.guazi.com/bj/benz/o1/#bread')

for i in range(40):
    Tcase = driver.find_element_by_xpath("/html/body[@class='list']/div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li["+str(i+1)+"]/a[@class='car-a']/h2[@class='t']")
    price = driver.find_element_by_xpath("/html/body[@class='list']/div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li["+str(i+1)+"]/a[@class='car-a']/div[@class='t-price']/p")
    xinxi = driver.find_element_by_xpath("/html/body[@class='list']/div[@class='list-wrap js-post']/ul[@class='carlist clearfix js-top']/li["+str(i+1)+"]/a[@class='car-a']/div[@class='t-i']")
    print(Tcase.text)
    print(price.text)
    print(xinxi.text)