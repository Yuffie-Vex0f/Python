f=open('i_have_a_dream.txt','r',encoding='ansi')
speech_text=f.read()
f.close()
speech=speech_text.lower().split()
dic={}
for word in speech:
    if word not in dic:
        dic[word]=1
    else:
        dic[word]+=1
swd=sorted(list(dic.items()),key=lambda lst:lst[1],reverse=True)
for kword,times in swd:
    print(kword,times)
