import requests

url='https://www.facebook.com/search/posts/?q=%23sichuanfood'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'}


re=requests.get(url=url,headers=headers)
print(re)
print(re.text)
