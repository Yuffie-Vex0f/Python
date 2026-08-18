# 例 3-10：用莱布尼茨级数计算 π 的近似值
# π/4 ≈ 1 - 1/3 + 1/5 - 1/7 + 1/9 - ...
# 直到最后一项的绝对值小于  10⁻⁶ 为止

fm = 1
jg = 1
fh = 1
total = 0
while abs(jg) >= 1e-16:
    total += jg
    fh = -fh
    fm = fm + 2
    jg = fh / fm
print (f"PI值为：{total * 4}")

import math
fm = 1
fh = 1
jg = 1
total = 0

while math.fabs(jg) >= 1e-6:
    total = total + jg
    fh = -fh
    fm = fm + 2
    jg = fh / fm
print (f"Pi的近似值是{total * 4}")
    
# 用for循环把输入的英文变成反过来的
# word = input("请输入英文：")
# new_word = word[::-1]
# print (new_word)
# word = input("请输入英文：")
# new_word = ""
# for i in word:
#     new_word = i + new_word 
# print (new_word)

#输出一个完整的 9×9 方阵
# for a in range(1,10):
#     for b in range(1,10):
#         print (f"{a}*{b}={a*b:2d}" , end="\t")
#     print()

# for a in range(1,10):
#     for b in range(1,10):
#         print (f"{a}*{b}={a*b:2d}",end="\t")
#     print()

# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i}*{j}={i*j:2d}", end="\t")
#     print()   # 内层循环结束后换行

#   山 外 山
# + 青 龙 山
# ----------
#  青 龙 山 外
# 已知 4 个替代数字的文字中没有重复，编写程序求出文字所代表的数字。

# for qing in range(1,10):
#     for long in range(10):
#         for shan in range(1,10):
#             for wai in range(10):
#                 if len({qing,long,shan,wai}) < 4:
#                     continue
                
#                 left = qing*1000 + long*100 + shan*10 + wai 
#                 right = shan*100 + wai*10 + shan + qing*100 + long*10 + shan

#                 if left == right:
#                     print (f"qing={qing},long={long},shan={shan},wai={wai}")
#                     exit()
