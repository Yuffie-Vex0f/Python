w = float(input("输入："))
t = float(input("输入："))
BMI = w / t ** 2
print (f"BMI:{BMI:.1f}")
if BMI < 18.5:
    print("偏瘦")
elif 18.5 <= BMI <= 24:
    print ("正常")
elif 24 <= BMI <= 28:
    print ("超重")
else:
    print ("肥胖")
