# 使用 update() 将 dict2 合并到 dict1 中（观察相同键 'b' 的覆盖情况）
# 使用 get() 方法安全获取键 'f' 的值，不存在时返回 0
# 添加新键值对 'f': 7
# 使用 pop() 删除键 'c' 并返回其值
# 将 dict1 的所有键转换为集合 keys_set
# 对 keys_set 与集合 {'a', 'd', 'e'} 进行交集运算
# 使用 items() 遍历最终字典，输出所有键值对

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'd': 5, 'e': 6}

# dict1.update(dict2)

# print(dict1)

# print(dict1.get('f',0))

# dict1['f'] = 7
# print(dict1)

# dict1.pop('c')
# print(dict1)

# key_set = set(dict1)
# print(key_set)

# print(key_set & {'a', 'd', 'e'})

# print(dict1.items())



# 输入一串用逗号分隔的整数（如 "3,7,3,9,12,7,5,9"），完成以下所有操作：
# 用 split(',') 拆分成字符串列表
# 用列表推导式将字符串列表转换为整数列表
# 用集合对整数列表去重，得到不重复数字的集合
# 用集合推导式从原整数列表中筛选出偶数（同时自动去重）
# 用字典推导式统计每个不同数字出现的次数 {数字: 次数}
# 用 items() + 元组解包遍历字典，找出出现次数最多的数字
# 将所有不同数字按升序排序，用 join() 拼接成字符串输出

i = input("输入一串用逗号分隔的整数").split(',')

new_i = [int(ni) for ni in i ]
si = set(new_i)
new_si = {f for f in new_i if f % 2 == 0 }
dic = {num:new_i.count(num) for num in set(new_i)}
num  = [num for num,count in dic.items() if count == max(dic.values())]
so = sorted(si)
new_so = ','.join(map(str,so))
print(new_so)