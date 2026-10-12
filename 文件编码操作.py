#UTF-8通用编码
#文件操作，打开，读写，关闭
#打开文件open函数open(name,mode->文件操作读写或新建,encoding->编码格式)
f=open(r'C:\Users\34395\Desktop\poem_test.txt', 'r', encoding='utf-8')
print(f.read())#括号内表示读取多少字节
f=open(r'C:\Users\34395\Desktop\poem_test.txt', 'r', encoding='utf-8')
print(f.readlines())#结果为每一行内容构成的列表
f=open(r'C:\Users\34395\Desktop\poem_test.txt', 'r', encoding='utf-8')
print(f.readline())#与上面区分，一次只读取一行内容
print(f.readline())
print(f.readline())
#for循环读取文件操作
f=open(r'C:\Users\34395\Desktop\poem_test.txt', 'r', encoding='utf-8')
for line in f:#for循环读取文件
    print(f'每一行的内容是：{line}')
f.close()#关闭文件,解除文件占用
#with open（） as 语句
with open(r'C:\Users\34395\Desktop\poem_test.txt', 'r', encoding='utf-8') as f:
    for line in f:print(f'每一行的内容是：{line}')#执行完自动close文件避免遗忘

