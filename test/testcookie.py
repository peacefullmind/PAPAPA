import requests

r1 = requests.post('http://www.yourapp.com/login')
r2 = requests.post('http://www.yourapp.com/somepage',cookies=r1.cookies)