#读取文件 备份文件 丢弃标记为“测试”的数据
fr=open("D:\账单数据.txt","r",encoding="utf-8")
#print(fr.read())
fw=open("D:/ bill.txt","w",encoding="utf-8")#创建新文件
for line in fr:
    line=line.strip()#取消空格和换行符
    if line.split(",")[4]=="测试":
        continue
    fw.write(line)
    fw.write("\n")#手动换行
fw.close()#自带flush更新操作
fr.close()
fw=open("D:/ bill.txt","r",encoding="utf-8")
print(fw.read())




