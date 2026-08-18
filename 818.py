# 编写一个程序将分钟转换为秒。
# 定义函数convert_to_seconds()，参数为minutes。
# 在函数内，将分钟转换为秒（1分钟=60秒），并返回结果。
# class convert:
#     def convert_to_seconds(self , minutes):
#         seconds = minutes * 60
#         print(seconds)
# if __name__ == "__main__":
#     result = convert()
#     result.convert_to_seconds(60)
# class convert:
#     def convert_to_seconds(self , minutes):
#         seconds = minutes * 60
#         return seconds
# if __name__ == "__main__":
#     result = convert()
#     seconds_result = result.convert_to_seconds(60)
#     print(seconds_result)

# 编写一个程序将字符串转换为整数。
# 定义函数convert_to_int()，参数为str_number。
# 在函数内，将字符串参数转换为整数并返回。
# class convert:
#     def convert_to_int(self , str_number):
#         int_number = int(str_number)
#         return int_number
# if __name__ == "__main__":
#     result = convert()
#     int_result = result.convert_to_int("90")
#     print(int_result)

# 编写一个程序，找出列表中最大和最小数字之间的差值。
# 定义函数difference_max_min()，参数为list_nums。
# 在函数内部，找出列表中的最大和最小数字，并返回差值
# class deiierent:
#     def different_max_min(self , list_nums):
#         d = max(list_nums) - min(list_nums)
#         return d
# if __name__ == "__main__":
#     result = deiierent()
#     d_result = result.different_max_min([1,2,3,4,5])
#     print(d_result)

# 编写一个程序，返回整数列表中的最后一个元素。
# 定义函数last_element()的函数，参数为列表my_list。
# 在函数中，返回列表的最后一一个元素。
# class last:
#     def last_element(self , my_list):
#         laste = my_list[-1]
#         return laste
# if __name__ == "__main__":
#     result = last()
#     last_result = result.last_element([1,2,3,4,5])
#     print(last_result)

# 编写一个程序来检查两个字符串是否具有相同数量的字符。
# 定义函数compare_length()，有两个参数str1和str2。
# 在函数内，如果str1的长度等于str2的长度，则返回True，否则返回False
# class compare:
#     def compare_length(self , str1 , str2):
#         if len(str1) == len(str2):
#             return True
#         else :
#             return False
# if __name__ == "__main__":
#     result = compare()
#     len_result = result.compare_length("cbnjf","uaahsdasbd")
#     print(len_result)

# 编写一个程序来连接字符串的首尾字符。
# 定义函数join_first_last()，参数为input_str。
# 在函数内部，返回字符串的首尾字符的连接字符串。
# class join:
#     def join_first_last(self,input_str):
#         j = input_str[0] + input_str[-1]
#         return j
# if __name__ == "__main__":
#     result = join()
#     join_result = result.join_first_last("asdhasjk")
#     print(join_result)

# 编写一个程序来判断一个单词是否为复数。
# 定义函数is_plural()，参数为term(输入的单词)。
# 在函数内，如果单词以s结尾，则返回True，否则返回False。
# class is_:
#     def is_plural(self,term):
#         if term[-1] == "s":
#             return True
#         else:
#             return False
# if __name__ == "__main__":
#     result = is_()
#     is_result = result.is_plural("dadasafs")
#     print(is_result)

# 编写一个程序，用于在一组整数中找出唯一的数字。假设列表中只有一个唯一的数字。
# 定义函数find_unique_number()，参数为num_list，数字列表。
# 在函数内部，找出只出现一次的数字，并返回它。
# 如果列表只有一个数字，则返回该数字。
# 如果列表为空，则返回None。
# 如果不存在这样的数字，则返回None。
# def find_unique_number(num_list):
#     if num_list == []:
#         return None
#     if len(num_list) == 1:
#         return num_list[0]
#     dic = {}
#     for num in num_list:
#         dic[num] = dic.get(num,0)+1
#     for num,count in dic.items():
#         if count == 1:
#             return num
#     return None
# print(find_unique_number([1,1,2,2,3,4,3]))  

# 编写一个程序，创建一个给定范围内的整数列表。
# 定义函数list_between()，有两个参数start和end。
# 在函数内，创建一个介于start（不包括）和end（不包括）之间的所有整数的列表，并返回该列表。
# class lists:
#     def list_between(self,start,end):
#         start_list = list(range(start+1,end))
#         return start_list
# if __name__ == "__main__":
#     result = lists()
#     list_result = result.list_between(1,5)
#     print(list_result)

# 编写一个程序来判断一个数字是否为素数。
# 定义函数check_prime()，参数为一个数字。
# 在函数内，如果数字为素数，返回True，否则返回False。
# class check:
#     def check_prime(self,n):
#         if n <= 1:
#             return False
#         if n == 2:
#             return True
#         if n % 2 == 0:
#             return False
#         i = 3
#         while i * i <= n:
#             if n % i == 0:
#                 return False
#             i += 2
#         return True
# if __name__ == "__main__":
#     result = check()
#     check_result = result.check_prime(49)
#     print(check_result)