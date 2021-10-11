import re

# # num=input("输入：")
# # pattern=re.compile(r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$')
# #
# # getnum=re.findall(pattern,num)
# # print(getnum)
# pat=re.compile("AA")
# m=pat.search("DDDDDDAAAAsgs")
#
# print(m)
#
# #没有模式对象
# m2=re.search("AA","fagggAAgga")
# print(m2)
#
# # 前面是规则（正则表达式，后面是被校验的字符串）
# m3=re.findall("AA","safafagAAAfaf")
# print(m3)
#
# m4=re.findall("[A-Z]+","safafagAAAfafBBB")
# print(m4)
#
# # 找到a,用A替换，在第三个字符串中查找
# print(re.sub("a","A","abagafagga"))
#
# # 建议在被校验的字符串前面加上r，不用担心转义的问题
# a=r"\aaaaa-\'"
# print(a)



text="""
"D:\SOFTWARE\Program Files2\python\python.exe" D:/PYcode/PAPAPA/doubanTop/getdata.py
<div class="item">
<div class="pic">
<em class="">1</em>
<a href="https://movie.douban.com/subject/1292052/">
<img alt="肖申克的救赎" class="" src="https://img2.doubanio.com/view/photo/s_ratio_poster/public/p480747492.jpg" width="100"/>
</a>
</div>
<div class="info">
<div class="hd">
<a class="" href="https://movie.douban.com/subject/1292052/">
<span class="title">肖申克的救赎</span>
<span class="title"> / The Shawshank Redemption</span>
<span class="other"> / 月黑高飞(港)  /  刺激1995(台)</span>
</a>
<span class="playable">[可播放]</span>
</div>
<div class="bd">
<p class="">
                            导演: 弗兰克·德拉邦特 Frank Darabont   主演: 蒂姆·罗宾斯 Tim Robbins /...<br/>
                            1994 / 美国 / 犯罪 剧情
                        </p>
<div class="star">
<span class="rating5-t"></span>
<span class="rating_num" property="v:average">9.7</span>
<span content="10.0" property="v:best"></span>
<span>2337898人评价</span>
</div>
<p class="quote">
<span class="inq">希望让人自由。</span>
</p>
</div>
</div>
</div>

"""

pat=re.compile(r'<span class="title">(.*)</span>')
num=re.findall(pat,text)[1]
num=num.strip()
num.replace("/","")
print(num)