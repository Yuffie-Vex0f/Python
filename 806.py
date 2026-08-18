# 有一筐鸡蛋，1个1个地拿，正好拿完；2个2个地拿，还剩1个；3个3个地拿，正好拿完；4个4个地拿，还剩1个；
# 5个5个地拿，还差1个；6个6个地拿，还剩3个；7个7个地拿，正好拿完；8个8个地拿，还剩1个；9个9个地拿，正好拿完。问筐里最少有多少个鸡蛋？
# j = 0
# e = (0,1,0,1,4,3,0,1,0)

# while True:
#     egg = 1
#     for i in range(1,10):
#         if j % i != e[i-1]:
#             egg = 0
#     if egg == 1:
#         print("j=",j)
#         break
#     j += 1

# p = []
# j = [1,2,3,4,5,6,7,8]
# for i in j:
#     p.append(i)
# print(p)

# p = [i for i in [1,2,3,4,5,6,7,8]]
# print(p)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 20, 'd': 4}

# # 只从 dict2 更新 dict1 中的 'b' 和 'd'
# keys_to_update = {'b', 'd'}
# dict1.update({k: v for k, v in dict2.items() if k in keys_to_update})
# print(dict1)  # {'a': 1, 'b': 20, 'c': 3}  ← d 不在 dict1 中，所以没加入

# lst = [3,2,1]
# lst.append(lst)

# s = ['a','b','c']
# s[0] = "l"
# print(s)