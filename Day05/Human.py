#  定义一个父类函数 当函数内的方法什么逻辑都没有，也就是直接pass结束时，则被认定是个抽象方法
class Human:
    def eat(self):
        pass


class Teacher(Human):
    def aaa(self):
        print("这是老师")


class Student(Human):
    def bbb(self):
        print("这是学生")


human = Human()
human.eat()

