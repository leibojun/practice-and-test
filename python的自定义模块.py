import module1#这里引入了自定义模块module
module1.func1(1,2,6)#使用了功能“func1”
from module1 import*#虽然是全部引用，但是模块里all=func1，所以只能引用到func1，但是func2可以手动导入
func1(3,4,5)
###########python包是一个文件夹，里面包含很多python模块