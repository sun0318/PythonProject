class Student:
    class_name = "五班"

    def act(self):
        print("学生上课")

    def same(self):
        print("同名方法1")


class Human:
    height = None

    def eat(self):
        print("人吃饭")

    def same(self):
        print("同名方法2")


# 类后面加类名表示继承，可以多继承； 如果父类有同名的方法，会优先第一个
class StudentInformation(Student, Human):
    name = None
    age = None
    address = None

    # def __init__(self, name, age, address, num):
    #     self.name = name
    #     self.address = address
    #     self.age = age
    #     print(f"学生信息{num}录入完成，信息为：【学生姓名：{name}，年龄：{age}，地址：{address}】")

    def eat(self):
        print("人不用每天吃饭")


# for i in range(0, 3):
#     i = i + 1
#     print(f"当前录入第{i}位学生信息，总共需录入3位学生信息")
#     name = input("请输入学生姓名：")
#     age = input("请输入学生年龄：")
#     address = input("请输入学生地址：")
#     # stu = StudentInformation(name, age, address, i)
#     stu = StudentInformation(name, age, address, i)

stu = StudentInformation()
# stu.eat()
# stu.same()
# stu.act()
#  调用父类方法或属性 父类名.  或者  super().
#  但是注意，当一个类继承了多个父类时，就用不了super()了，因为不确定是调用哪个父类的方法
print(Student.class_name)
func = getattr(stu,"eat")
func()
