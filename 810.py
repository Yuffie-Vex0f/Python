# max_bw , max_dj = 31.2333 , 121.55
# min_bw , min_dj = 31.2222 , 121.45

# # with open("V:\\专升本\\Python程序设计基础\\第五章\\car_data.txt",'r',encoding='utf-8') as car:
# #     lst = car.readlines()
# # new_car = [s[:-1].split(',') for s in lst]
# lst = list(open("V:\\专升本\\Python程序设计基础\\第五章\\car_data.txt",'r',encoding = 'utf-8'))
# # car = [s[:-1].split(',') for s in lst]
# car = []
# for s in lst:
#     carone = s[:-1].split('||')
#     car.append(carone)
# print('在该区域出现的车辆有：')
# for t in range(len(car)):
#     if (min_bw < float(car[t][2]) < max_bw) and (min_dj < float(car[t][3]) < max_dj) :
#         print('时间：%s\t车牌：%s\t北纬：%s,东经：%s' % (car[t][0], car[t][1], car[t][2], car[t][3]))


# with open("V:\\专升本\\Python程序设计基础\\第五章\\i_have_a_dream.txt" , 'r' , encoding='GBK') as f:
#     speech_text = f.read()
# speech = speech_text.lower().split()
# dic = {}
# for word in speech:
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] += 1
# swd = sorted(list(dic.items()) , key = lambda lst:lst[1] , reverse = True)

# with open("V:\\专升本\\Python程序设计基础\\第五章\\stop_word_list.txt" , 'r' , encoding = 'GBK') as sw:
#     stop_word = sw.read()

# count = 0
# for kword,times in swd:
#     if kword not in stop_word:
#         print(kword,times)
#         count += 1
#         if count == 10:
#             break

# import jieba
# import wordcloud

# with open("V:\\专升本\\Python程序设计基础\\第五章\\荷塘月色.txt" , 'r' , encoding='ANSI') as text:
#     zzq = text.read()
# art = jieba.lcut(zzq)
# dic = {}
# for word in art:
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] += 1

# sot = sorted(list(dic.items()) , key = lambda lst:lst[1] , reverse = False)
# with open("V:\\专升本\\Python程序设计基础\\第五章\\中文虚词列表.txt" , 'r' , encoding='ANSI') as stop:
#     stop_word = stop.read()
# wordcloud_dic = []
# for kword,times in sot:
#     if kword not in stop_word and times > 1:
#         wordcloud_dic.append(kword)


# w = wordcloud.WordCloud(background_color='white',
#                         width=150,
#                         height=120,
#                         max_font_size=48,
#                         font_path='C:/Windows/Fonts/simhei.ttf')
# text = ' '.join(wordcloud_dic)
# w.generate(text)
# w.to_file('V:\\专升本\\Python程序设计基础\\第五章\\test.png')

# with open("V:\\专升本\\Python程序设计基础\\第五章\\file1.txt" , 'r' , encoding='ANSI') as file1:
#     line = file1.readlines()
#     line_count = len(line)

#     word = 0
#     for words in line:
#         word += len(words)
#     word = sum([len(words) for words in line])
#     print(line_count)
#     print(word)

# with open("V:\\专升本\\Python程序设计基础\\第五章\\file1.txt" , 'r' , encoding='ANSI') as file1:
#     lines = file1.readlines()

# with open("V:\\专升本\\Python程序设计基础\\第五章\\file21.txt" , 'w' , encoding='ANSI') as file2:
#     for line in reversed(lines):
#         file2.write(line)

# students = []

# with open("V:\\专升本\\Python程序设计基础\\第五章\\score.txt" , 'r' , encoding='ANSI') as score:
#     lines = score.readlines()
    
#     for line in lines[1:]:
#         line = line.strip()
#         parts = line.split()
#         # print(len(parts), parts) 
#         stu_id = parts[0].strip()
#         daily = float(parts[1].strip())
#         final = float(parts[2].strip())
#         total = daily * 0.4 + final * 0.6
#         students.append((stu_id, daily, final, total))

# with open("V:\\专升本\\Python程序设计基础\\第五章\\810.txt", 'w', encoding='ANSI') as f:
#     f.write("学号\t总评成绩\n")
#     for stu_id, daily, final, total in students:
#         f.write(f"{stu_id}\t{total}\n")

# total_students = len(students)

# count_90 = 0
# count_80 = 0
# count_70 = 0
# count_60 = 0
# count_below = 0

# total_sum = 0

# for stu_id , daily , final , total in students:
#     total_sum += total
#     if total >= 90:
#         count_90 += 1
#     elif total >= 80:
#         count_80 += 1
#     elif total >= 70:
#         count_70 += 1
#     elif total >= 60:
#         count_60 += 1
#     else:
#         count_below += 1
# avg = total_sum / total_students

# print("=" * 40)
# print(f"学生总人数：{total_students}")
# print(f"班级总平均分：{avg:.2f}\n")

# print("各分数段人数分布：")
# print(f"  90分以上（含90）：{count_90} 人")
# print(f"  80~89分：{count_80} 人")
# print(f"  70~79分：{count_70} 人")
# print(f"  60~69分：{count_60} 人")
# print(f"  60分以下：{count_below} 人")


# with open("V:\\专升本\\Python程序设计基础\\第五章\\中文虚词列表.txt" , 'r' , encoding='ANSI') as stop:
#     stop_word = stop.read()
# wordcloud_dic = []
# for kword,times in sot:
#     if kword not in stop_word and times > 1:
#         wordcloud_dic.append(kword)

# import jieba
# import wordcloud

# with open("V:\\专升本\\Python程序设计基础\\第五章\\荷塘月色.txt" , 'r' , encoding='ANSI') as text:
#     zzq = text.read()
# art = jieba.lcut(zzq)
# dic = {}
# for word in art:
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] += 1


# import jieba
# import wordcloud
# import pdfplumber

# with pdfplumber.open("V:\\专升本\\Python程序设计基础\\第五章\\十五五.pdf") as siz:
#     report = ""
#     for page in siz.pages:
#         report += page.extract_text()
# f = jieba.lcut(report)
# dic = {}
# for word in f:
#     if len(word) <= 1:
#         continue
#     if word not in dic:
#         dic[word] = 1
#     else:
#         dic[word] += 1

# suum = []
# for word , count in dic.items():
#     if count > 100:
#         suum.append(word)
# w = wordcloud.WordCloud(background_color='white',
#                         width=600,
#                         height=480,
#                         max_font_size=48,
#                         font_path='C:/Windows/Fonts/simhei.ttf')
# w.generate_from_frequencies(dic)
# w.to_file("V:\\专升本\\Python程序设计基础\\第五章\\十五五.png")


# 编写一个Python程序，计算并输出斐波那契数列的前20项。斐波那契数列的定义如下：
# F(0)=0, F(1)=1
# F(n)=F(n-1)+F(n-2) (n≥2)

# fib = [0,1]

# for i in range(2,20):
#     next_fib = fib[i-1]+fib[i-2]
#     fib.append(next_fib)
# for r,value in enumerate(fib,start=1):
#     print(f"{r},{value}")

# 编写一个Python程序，读取一个文本文件input.txt，统计其中每个单词出现的次数，并将结果按单词字典序输出到文件output.txt中。
# with open("V:\\专升本\\Python程序设计基础\\index.txt" , 'r' , encoding="utf-8") as eng:
#     lish = eng.read()
# english = lish.lower().split()

# count = {}

# for i in english:
#     if i not in count:
#         count[i] = 1
#     else:
#         count[i] += 1
# dic = sorted(count.items())

# with open("V:\\专升本\\Python程序设计基础\\output.txt" , 'w' , encoding="utf-8") as out:
#     for word , num in dic:
#         out.write(f"{word}:{num}")

import re  # 正则表达式模块

with open("V:\\专升本\\Python程序设计基础\\index.txt", 'r', encoding="utf-8") as eng:
    content = eng.read()

# 使用正则表达式只提取英文字母组成的单词（包括连字符）
# 注意：这里只提取 a-z 和 A-Z 的单词，数字和标点会被忽略
words = re.findall(r"[a-zA-Z]+(?:-[a-zA-Z]+)*", content)  # 支持连字符如 sakura-fubuki

# 转为小写并统计
word_count = {}
for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

# 排序并输出
with open("V:\\专升本\\Python程序设计基础\\output.txt", 'w', encoding="utf-8") as out:
    for word, count in sorted(word_count.items()):
        out.write(f"{word}: {count}\n")

print("统计完成！")