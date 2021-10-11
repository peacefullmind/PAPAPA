import requests

session = requests.Session()
# 这样写不对，cookie写成字典形式
# cookie='g4.lockflag=0; eredg4.login.account=18000415; eredg4.login.userid=10005157; JSESSIONID=308578836EF5A97222DEEE55F2C7E808'
User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

url1='http://25.1.0.207:8080/DAS/login.go?reqCode=init'
data1={'account':'MTgwMDA0MTU=','password':'QWJjZGVAMTIz'}
data2={'account':'18000415','password':'Abcde@123'}
r1=session.post(url=url1,data=data2)
print(r1.text)

urlq='http://25.1.0.207:8080/DAS/index.go?reqCode=indexInit'
myurl='http://25.1.0.207:8080/DAS/durationManage.go?reqCode=queryDurationManageForManage'
data={"start": "0","limit": "500","accountingYear": "2020","accountingMonth": "12","accountingScope": "S001","queryParam":'',"loginuserid": "10005157",}
r2=session.post(url=urlq,data=data)
print('===========================')
print(r2.text)
