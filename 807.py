# 使用列表推导式生成 1 到 n 的平方数列表，并输出。

# n = int(input("请输入n:"))
# lst = [i**2 for i in range(1,n+1)]
# print(lst)

# 使用列表推导式，从 1 到 n 中筛选出所有偶数，并输出结果列表。

# n = int(input("请输入n:"))
# os = [i for i in range(1,n+1) if i % 2 == 0]
# print(os)

# 给定一个由多个单词组成的列表，使用列表推导式将其中所有单词转换为大写形式，并输出新列表。

# word = input("请输入单词列表（用空格分隔）：")
# lst = [i.upper() for i in word ]
# print(lst)
# lst = []
# for i in word:
#     lst.append(i.upper())
# print(lst)

# 输入一个句子，使用列表推导式筛选出其中长度大于3的单词，并输出筛选后的列表。

# sentence = input("请输入句子：").split()
# long_word = [i for i in sentence if len(i) > 3]
# print(long_word)

# 使用字典推导式，生成一个字典，键为 1 到 n 的整数，值为该整数的平方。

# n = int(input("请输入n:"))
# pf = {i:i**2 for i in range(1,n+1)}
# print(pf)

# 输入一个字符串，使用字典推导式统计每个字符出现的次数（不使用 collections.Counter）

# st = input("请输入字符串：")
# out = {i:st.count(i) for i in st }
# print(out)

# 输入一个整数列表（用空格分隔），使用集合推导式筛选出其中的偶数，并自动去重，输出结果集合

# lst = input("请输入整数列表：").split()
# lst = [int(i) for i in lst]
# se = {i for i in lst if i % 2 == 0}
# print(se)

# 使用嵌套列表推导式生成九九乘法表中所有 x * y 的乘积，要求 x >= y，每个乘积以元组 (x, y, x*y) 形式存储，输出完整列表

# bp = [(x,y,x*y) for x in range(1,10) for y in range(1,10) if x >= y]
# print(bp)

# 输入一个包含多个单词的列表，使用列表推导式将每个单词首字母大写（其余字母不变），然后用空格连接成新字符串并输出

# word = input("请输入单词列表（用空格分隔）：").split()
# sentence = [i[0].upper() + i[1:] for i in word]
# new_word = " ".join(sentence)
# print(new_word)

# 给定一个学生名单列表（姓名 + 分数，用空格分隔），使用字典推导式将其转换为字典 {姓名: 分数}，然后使用列表推导式筛选出分数大于等于60的学生姓名，输出及格名单。
# lst = input("请输入学生成绩（姓名 分数，用空格分隔）：").split()
# pairs = [(lst[i],int(lst[i+1])) for i in range(0,len(lst),2) ]
# dic = {name:score for name,score in pairs}
# passed = [name for name , score in dic.items() if score >= 60]
# print(f"及格名单：{passed}")

# a = [i * 3 for i in range(6)]
# a = []
# for i in range(6):
#     i = i*3
#     a.append(i)
# print(a)

# b = [x for x in "Python" if x not in "aeiou"]
# b = []
# for x in "Python":
#     if x not in "aeiou":
#         b.append(x)
# print(b)

# c = [(i, j) for i in range(3) for j in range(3) if i + j > 2]
# c = []
# for i in range(3):
#     for j in range(3):
#         if i + j > 2:
#             c.append((i,j))
# print(c)

# d = {word: len(word) for word in ["apple", "banana", "cherry"] if len(word) > 5}
# d = {}
# for word in  ["apple", "banana", "cherry"]:
#     if len(word) > 5:
#         d[word] = len(word)
# print(d)

# scores = {"张三": 85, "李四": 59, "王五": 92, "赵六": 73}
# passed = {name: score for name, score in scores.items() if score >= 60}
# print(passed)

# scores = {"张三": 85, "李四": 59, "王五": 92, "赵六": 73}
# passed = {}
# for name,score in scores.items():
#     if score >= 60:
#         passed[name] = score
# print(passed)

# 输入一个英文句子，完成以下操作：
# 使用 split() 将句子拆分为单词列表
# 使用列表推导式筛选出长度 ≥ 4 的单词，并全部转为小写
# 使用集合对筛选结果自动去重
# 输出去重后的单词集合，以及单词总数

# sentence = input("输入一个英文句子：").split()
# words = [i.lower() for i in sentence if len(i) >= 4]
# word = set(words)
# print(
#     f"去重后的单词：{word}\n"
#     f"单词总数：{len(word)}"
# )

# 初始列表 nums = [5, 2, 8, 1, 9, 3]，依次执行以下操作，每一步都输出当前列表：
# 在列表末尾添加元素 7
# 在列表索引2的位置插入元素 4
# 使用切片取出索引 1~4 的子列表并输出（不修改原列表）
# 删除列表中第一次出现的 2
# 对列表进行升序排序
# 使用 pop() 移除并返回最后一个元素

# nums = [5, 2, 8, 1, 9, 3]
# nums.append(7)
# nums.insert(2,4)
# num = nums[1:5]
# nums.remove(2)
# nums.sort()
# nums.pop()
# print(nums)

# 使用 zip() 将两个列表打包成元组列表
# 使用字典推导式将元组列表转换为字典 {姓名: 分数}
# 使用 items() 遍历字典，通过元组解包获取姓名和分数
# 计算平均分，并输出所有高于平均分的学生姓名（用列表推导式）

# names = ["Alice", "Bob", "Charlie", "Diana"]
# scores = [85, 92, 78, 88]

# new = zip(names,scores)
# dic = {name:score for name,score in new }
# nam = [named for named,scored in dic.items() ]
# scor = sum([scored for named,scored in dic.items()]) / 4
# new_name = [nn for nn,ns in dic.items() if ns > scor]
# print(new_name)