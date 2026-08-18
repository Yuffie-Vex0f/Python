# 1．编写程序，从键盘输入两点的坐标(x1,y1)和(x2,y2)，计算并输出两点之间的距离。
# from math import sqrt 

# x1 = float(input("请输入坐标x1:"))
# x2 = float(input("请输入坐标x2:"))
# y1 = float(input("请输入坐标y1:"))
# y2 = float(input("请输入坐标y2:"))

# result = sqrt((x1-x2)**2 + (y1-y2)**2)
# print (f"两点之间的距离为：{result:.2f}")

# 2．编写程序，从键盘输入年份值和月份值，输出该年当月的日历（调用calendar模块中的month( )函数）。
# import calendar

# year = int(input("输入年份值:"))
# mon = int(input("输入月份值:"))
# table = calendar.month(year,mon)
# print(f"该年当月的日历{table}")

# 3．编写程序，产生两个10以内的随机整数，以第1个随机整数为半径、第2个随机整数为高，计算并输出圆锥体的体积。
# import random
# from math import pi

# r = random.randint(1,10)
# h = random.randint(1,10)
# v = (pi/3)*r**2*h
# print(f"圆锥体的体积为:{v:.2f}")

# 4．编写程序，从键盘输入一个年份值，判断该年是否为闰年并输出判断结果。（提示：若该年份值能被4整除且不能被100整除或者该年份值能被400整除，则该年是闰年，否则不是。）
# year = int(input("输入一个年份值:"))

# if  (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print(f"{year}年是闰年")
# else:
#     print(f"{year}年不是闰年")

# 5．编写程序，从键盘输入三个数，计算并输出三个数中最大的数。
# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# c = float(input("请输入第三个数字："))

# if a >= b and a >= c:
#     print(f"三个数中最大的数是{a:.2f}")
# elif b >= a and b >= c:
#     print(f"三个数中最大的数是{b:.2f}")
# else:
#     print(f"三个数中最大的数是{c:.2f}")

# max_num = max(a,b,c)
# print(f"三个数中最大的数是{max_num:.2f}")

# 6．编写程序，从键盘输入三个数，实现三个数从小到大排序并输出结果。
# a = float(input("请输入第一个数字："))
# b = float(input("请输入第二个数字："))
# c = float(input("请输入第三个数字："))

# max_num = max(a,b,c)
# min_num = min(a,b,c)
# other = (a+b+c)-max_num-min_num

# print(f"从小到大排序：{min_num:.2f}, {other:.2f}, {max_num:.2f}")

# 7．编写程序，从键盘输入a、b、c的值，计算一元二次方程ax2+bx+c=0的根，并根据b2-4ac的值大于0、等于0及小于0三种情况分别进行讨论。
# from math import sqrt
# a = int(input("请输入a:"))
# b = int(input("请输入b:"))
# c = int(input("请输入c:"))

# if b**2-4*a*c > 0:
#     result1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
#     result2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
#     print(f"一元二次方程ax2+bx+c=0的根为{result1}和{result2}")
# elif b**2-4*a*c == 0:
#     result = -b / (2*a)
#     print(f"一元二次方程ax2+bx+c=0的根为{result}")
# elif b**2-4*a*c < 0:
#     print(f"一元二次方程ax2+bx+c=0无解")

# from math import sqrt

# a = int(input("请输入a:"))
# b = int(input("请输入b:"))
# c = int(input("请输入c:"))

# if a == 0:
#     print("这不是一元二次方程（a不能为0）")
# else:
#     delta = b**2 - 4*a*c

#     if delta > 0:
#         result1 = (-b + sqrt(delta)) / (2 * a)
#         result2 = (-b - sqrt(delta)) / (2 * a)
#         print(f"一元二次方程有两个不同实根：{result1:.2f} 和 {result2:.2f}")
#     elif delta == 0:
#         result = -b / (2 * a)
#         print(f"一元二次方程有两个相同实根（重根）：{result:.2f}")
#     else:
#         # delta < 0
#         real_part = -b / (2 * a)
#         imag_part = sqrt(-delta) / (2 * a)
#         print(f"一元二次方程有两个共轭复根：{real_part:.2f} ± {imag_part:.2f}i")

# 8．编写程序，从键盘输入一个字符，如果是大写英文字母则将其转换为小写英文字母，如果是小写英文字母则将其转换为大写英文字母，其他字符原样输出。
# alphabet = input("请输入一个字符:")

# if len(alphabet) != 1:
#     print("请输入单个字符！")
# if len(alphabet) == 1 and alphabet.islower():
#     print(f"原字符转换为大写：{alphabet.upper()}")
# elif len(alphabet) == 1 and alphabet.isupper():
#     print(f"原字符转换为小写：{alphabet.lower()}")
# else:
#     print(f"返回原字符{alphabet}")

# alphabet = input("请输入一个字符:")

# if len(alphabet) != 1:
#     print("请输入单个字符！")
# else:
#     print(f"转换结果：{alphabet.swapcase()}")

# 9．编写程序，从键盘输入数字n，通过循环结构计算从1到n的乘积。
# n = int(input("输入数字n:"))
# begin = 1

# for i in range(1,n+1):
#     begin = begin*i
# print(f"从1到n的乘积是{begin}")

# n = int(input("输入数字n:"))

# if n < 0:
#     print("请输入非负整数！")
# else:
#     begin = 1
#     for i in range(1, n + 1):
#         begin *= i  # 简写：begin = begin * i
#     print(f"从1到n的乘积是{begin}")

# 10．编写程序，通过循环结构计算全部的水仙花数。水仙花数是一个三位数，该数正好等于组成该三位数的各位数字的立方和。例如，13+53+33=153。
# for i in range(100,1000):
#     a = i // 100
#     b = (i // 10) % 10
#     c = i % 10
#     if a**3 + b**3 + c**3 == i:
#         print(i)


# 11．编写程序，通过循环结构计算并输出满足条件的正方体的体积：正方体棱长从1到10，依次计算体积，当体积大于100时停止输出。
# for a in range(1,11):
#     v = a ** 3 
#     if v > 100:
#         break
#     print(f"棱长为{a},体积为{v}")

# 12．编写程序，从键盘输入一个整数并判断该数的类别：其因数之和等于数字本身的数称为完全数，比数字本身大的数称为丰沛数，比数字本身小的数称为不足数。
# num = int(input("请输入一个整数："))
# ys = []
# for i in range(1,num):
#     if num % i == 0:
#         ys.append(i)
# ys_sum = sum(ys)
# if ys_sum == num:
#     print("这个数字是完全数")
# elif ys_sum > num:
#     print("这个数字是丰沛数")
# elif ys_sum < num:
#     print("这个数字是不足数")

# 13．编写程序，使用双重循环结构输出如图3-18所示的运行结果。
# ![](./3-18.png)
# for i in range(1,5):
#     for n in range(4-i):
#         print(" ",end=" ")
#     for j in range(1,2*i):
#         print("*",end=" ")
#     print("\n")
# for i in range(3,0,-1):
#     for n in range(4 - i):
#         print(" ",end=" ")
#     for j in range(2 * i - 1):
#         print("*",end=" ")
#     print("\n")

# 14．编写程序，生成一个0～100之间的随机数，然后让用户尝试猜测这个数字。程序给出猜测方向（更大或更小）的提示，用户继续进行猜测，直到用户猜测成功或输入一个0～100以外的数字后退出游戏。
# import random


# rand = random.randint(0,100)

# while True:
#     guess = int(input("请输入猜测的数字："))
#     if rand > guess:
#         print("随机数更大，请继续猜测")
#     elif rand < guess and guess < 100:
#         print("随机数更小，请继续猜测")
#     elif rand == guess or guess > 100:
#         break
#    
# 15．编写程序，计算Fibonacci数列的前20项（Fibonacci数列的特点是，第1、2项的值都为1，从第3项开始，每项都是前两项之和）。

# a = 1
# b = 1

# print(f"第1项：{a}")
# print(f"第2项：{b}")

# for i in range(3,21):
#     c = a + b
#     print(f"第{i}项：{c}")
#     a , b = b , c

# 16．编写程序，从键盘输入两个正整数，计算两个数的最大公约数和最小公倍数。
# a = int(input("请输入第一个正整数："))
# b = int(input("请输入第二个正整数："))

# or_a = a
# or_b = b

# while b != 0:
#     a , b = b , a % b

# gcd = a
# lcm = or_a * or_b // gcd

# print(f"最大公约数是：{gcd}")
# print(f"最小公倍数是：{lcm}")
# import math

# a = int(input("请输入第一个正整数："))
# b = int(input("请输入第二个正整数："))

# gcd = math.gcd(a, b)
# lcm = a * b // gcd

# print(f"最大公约数：{gcd}")
# print(f"最小公倍数：{lcm}")

# 17．编写程序，判断一个整数是否为素数（判断整数x是否为素数，最简单的方法就是用2～x-1之间的所有整数逐一去除x，若x能被其中任意一个数整除，则x就不是素数，否则为素数）。

# x = int(input("请输入第一个整数："))

# if x < 2:
#     print(f"{x}不是素数")

# for i in range(2,x):
#     if x % i == 0 :
#         print(f"{x}不是素数")
#         break
# else:
#     print(f"{x}是素数")

    
# 18．编写程序，实现一个循环5次的计算小游戏，每次随机产生两个100以内的数字，让用户计算两个数字之和并输入结果，如果计算结果正确则加一分，如果计算结果错误则不加分。如果正确率大于或等于80%，则闯关成功。

# import random

# score = 0
# mf = 5

# for i in range(1,6):
#     a = random.randint(0,100)
#     b = random.randint(0,100)
#     s = a + b
#     print(f"第{i}题:第一个数字是{a}，第二个数字是{b}")
#     user_input = int(input("计算两个数字之和:"))

#     if s == user_input:
#         score = score + 1
#         print("回答正确加一分")
#     if s != user_input:
#         print("回答错误")

# print(f"你的得分是{score}")

# if score / mf >= 0.8:
#     print("闯关成功")
# else:
#     print("闯关失败")


# 19．编写程序，从键盘输入一个姓名（可能为2个字、3个字或4个字），将该姓名的第2个汉字修改为*号。如果索引出错，则进行异常处理并提示索引错误。

# name = input("请输入名字：")

# if len(name) == 1:
#     print("请输入2个字及以上：")

# else:
#     try: 
#         new_name = name[0] + '*' + name[2:]
#     except IndexError:
#         print("索引错误")
#     else:
#         print(f"{new_name}")

# 20．编写程序，从键盘输入用户名和密码，判断该用户名和密码是否均在文件information.txt中。若在，则提示用户名和密码正确，否则提示用户名和密码错误。如果文件打开失败，则进行异常处理并提示文件打开失败，否则关闭文件。无论文件打开成功与否，最后均会打印出输入的用户名和密码。

# username = input("请输入用户名：")
# password = input("请输入密码：")

# try:
#     file = open("information.txt" , 'r')
#     content = file.read()

#     if username in file and password in content:
#         print("用户名和密码正确")
#     else:
#         print("用户名和密码错误")
# except FileNotFoundError:
#     print("文件打开失败")
# else:
#     file.close()
#     print("关闭文件")
# finally:
#     print(f"输入用户名是{username}")
#     print(f"输入密码是{password}")