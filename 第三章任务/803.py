import calendar

r = "星期一星期二星期三星期四星期五星期六星期日"

while True:
    y = input('请输入年，输入 x 退出\n')
    if y in ('x','X'):
        break
    else:
        m = input("请输入月\n")
        d = input("请输入日\n")
        i = calendar.weekday(int(y),int(m),int(d))
        week = r[i*3:i*3+3]

        print(f"{y}年{m}月{d}日是{week}")