import requests

url = "https://tun.tmp.link/api_v2/file"

payload = "action=details&ukey=61163db0bfe73&token=mrmj1oarldt9bdrvvwjt"
headers = {
  'authority': 'tun.tmp.link',
  'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'sec-ch-ua-mobile': '?0',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'origin': 'https://app.tmp.link',
  'sec-fetch-site': 'same-site',
  'sec-fetch-mode': 'cors',
  'sec-fetch-dest': 'empty',
  'referer': 'https://app.tmp.link/',
  'accept-language': 'zh-CN,zh;q=0.9'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
