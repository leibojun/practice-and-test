#多态：同样的函数，传入不同的对象，得到不同的状态
class Animal:
    def speak(self):
        pass#由父类确定有那些方法，此时父类是一个抽象类，包含了一个抽象方法以供子类复写
class Dog(Animal):
    def speak(self):
        print("wolf wolf")
class Cat(Animal):
    def speak(self):
        print("meow meow")
def func(animal:Animal):#此处声明传入父类对象
    animal.speak()
dog = Dog()
cat = Cat()
func(dog)
func(cat)
