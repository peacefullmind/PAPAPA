str1="29.80万"
str2="2014年|8.5万公里|到店服务"

str1=str1.replace('万','')
print(str1)

str2=str2.split('|')
print(str2)
# str2[0].replace('年','')
# str2[1].replace('万公里','')
print(str1+','+str2[0].replace('年','')+','+str2[1].replace('万公里',''))
print(str2[0].replace('年','')+','+str2[1].replace('万公里','')+','+str1)