f1=open("1.jpg", "rb")
file_content=f1.read()
f1.close()

f2 = open("2.jpg", "wb")
filesize=f2.write(file_content)   #执行操作后返回写入字节数
print(filesize,'Bytes','复制成功')
f2.close()
