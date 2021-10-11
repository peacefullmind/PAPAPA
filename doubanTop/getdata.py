import requests
from bs4 import BeautifulSoup
import re
import xlwt
import sqlite3

def main():
    baseurl="https://movie.douban.com/top250?start="
    datalist=getData(baseurl)
    # savepath=".\\豆瓣电影Top250.xls"
    dbpath="movie.db"
    saveData2DB(datalist,dbpath)
    # saveData(datalist,savepath)

findLink=re.compile(r'<a href="(.*?)">')
# findImgSrc=re.compile(r'<img.*src=(.*?)"',re.S) #让换行符包含在字符中
findImgSrc=re.compile(r'<img.*src="(.*?)"',re.S) #让换行符包含在字符中
findTitle=re.compile(r'<span class="title">(.*)</span>')
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge=re.compile(r'<span>(\d*)人评价</span>')
findInq=re.compile(r'<span class="inq">(.*)</span>')
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)


def getData(baseurl):
    datalist=[]
    for i in range(0,10):
        url=baseurl+str(i*25)
        html=askURL(url)
        bs=BeautifulSoup(html,"html.parser")
        for item in bs.find_all('div',class_="item"):
            # print(item)
            item=str(item)

            data=[]
            link=re.findall(findLink,item)[0]
            data.append(link)
            imfSrc=re.findall(findImgSrc,item)[0]
            data.append(imfSrc)
            title=re.findall(findTitle,item)
            if(len(title)==2):
                ctitle=title[0]
                data.append(ctitle)
                otitle=title[1].replace("/","")
                data.append(otitle)
            else:
                data.append(title[0])
                data.append(' ')

            Rating=re.findall(findRating,item)[0]
            data.append(Rating)

            judgeNum=re.findall(findJudge,item)[0]
            data.append(judgeNum)

            inq=re.findall(findInq,item)
            if len(inq) !=0:
                inq=inq[0].replace("。","")
                data.append(inq)
            else:
                data.append(" ")

            bd=re.findall(findBd,item)[0]
            bd=re.sub("<br(\s+)?/>(\s+)?"," ",bd)
            bd=re.sub('/'," ",bd)
            data.append(bd.strip())

            print(data)
            datalist.append(data)
    # print(datalist)




    return datalist

def askURL(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
    }
    # url = "https://movie.douban.com/top250"
    res = requests.get(url, headers=headers)
    # print(res.text)
    return res.text

def saveData(datalist,savepath):
    book=xlwt.Workbook(encoding="utf-8",style_compression=0)
    sheet=book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)
    col=("电影链接","图片链接","中文名","外文名","评分","评价人数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])
    for i in range(0,250):
        print("第%d条" %i)
        data=datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])
    book.save('豆瓣电影Top250.xls')

def saveData2DB(datalist,dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index==4 or index==5:
                continue
            data[index]='"'+data[index]+'"'
        sql='''
                insert into movie250(info_link,pic_link,cname,ename,score,rated,instroduction,info)
                values (%s
                )
                ''' %",".join(data)
        print(sql)
        cursor.execute(sql)
        conn.commit()
    cursor.close()
    conn.close()


def init_db(dbpath):
    sql='''
        create table movie250
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            instroduction text,
            info text
        );
    '''
    conn=sqlite3.connect(dbpath)
    cursor=conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()


if __name__=="__main__":
    main()
    # init_db('testtt.db')
    print("end")


