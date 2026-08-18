L=list(open('bp.csv','r',encoding='GBK'))
##print(L)
dataList=[]
for s in L[1:]:
    dataList.append(s.split(','))
##print(dataList)

max_SBP=0    #假定一个不可能的最高收缩压
min_DBP=800  #假定一个不可能的最低舒张压
sum=0        #心率总计初值

for ls in dataList:
    if max_SBP<float(ls[1]):
        max_SBP=float(ls[1])
        max_SBP_time=ls[0]
    if min_DBP>float(ls[2]):
        min_DBP=float(ls[2])
        min_DBP_time=ls[0]
    sum+=float(ls[3][:-1])   #去掉换行符并转为浮点数
avg_HR=sum/len(dataList)
print('最高收缩压为{}，出现在{}'.format(max_SBP,max_SBP_time))
print('最低舒张压为{}，出现在{}'.format(min_DBP,min_DBP_time))
print('平均心率为',int(avg_HR))

