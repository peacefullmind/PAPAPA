import urllib.request
import re
import xlwt

def getdata():
    url='http://www.risfond.com/case/fmcg/26700'
    html=urllib.request.urlopen(url).read().decode('utf-8')
    print(html)

getdata()
