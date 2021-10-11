
mylist=["#a","##b","##c","###d","#e"]
outlist=[]
def Cal(mylist):
    start=0
    for r in mylist:
        recount={}
        for rr in r:
            recount[rr]=r.count(rr)
        num=recount['#']
        newstr=r.split("#")[-1]
        temp=[]
        temp.append(num)
        temp.append(newstr)
        outlist.append(temp)
# def Out(outlist):
#     for r in outlist:


Cal(mylist)
print(outlist)
outlist2=outlist

start=1
last_num=1
last_str=''
for r in outlist:
    start=start+1
    num=r[0]
    if(start==1):  #第一个位置
        outlist2[0]="1"
        last_num=1
        last_str="1"
    else:
        if(num)


