lst = list(open("V:\\专升本\\Python程序设计基础\\第五章\\BP.csv" , 'r' , encoding = 'GBK'))

data = [i.split(',') for i in lst[1:]]

max_ssy = 0
min_szy = 900
su = 0

for ls in data:
    if max_ssy < float(ls[1]):
        max_ssy = float(ls[1])
        max_time = ls[0]
    if min_szy > float(ls[2]):
        min_szy = float(ls[2])
        min_time = ls[0]
    su += float(ls[3][:-1])
avg = su / len(data)
# print('max=%s,time=%s'%(max_ssy,max_time))
# print('min=%s,time=%s'%(min_szy,min_time))
# print('avg=%s'%(avg))

# print('max={},time={}'.format(max_ssy,max_time))
# print('min={},time={}'.format(min_szy,min_time))
# print('avg=',avg)

print(f"max={max_ssy},time={max_time}")
print(f"min={min_szy},time={min_time}")
print(f"avg={avg}")
