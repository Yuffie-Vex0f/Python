min_n, min_e =31.2222, 121.45
max_n, max_e =31.2333, 121.55
LS=list(open('car_data.txt','r',encoding='utf-8'))
car=[]
for s in LS:
    carone=s[:-1].split('||')
    car.append(carone)
print('在该区间出现的车辆有：')
for t in range(len(car)):
    if (min_n<float(car[t][2])<max_n) and (min_e<float(car[t][3])<max_e):
        print('时间：%s\t车牌：%s\t北纬：%s,东经：%s' %(car[t][0],car[t][1],car[t][2],car[t][3]))
