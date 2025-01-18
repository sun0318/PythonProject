# 类里定义方法时，
# 注解方式 方法一 加# type，方法二 在变量后面加类型，如frequency: int，则是int类型

class Student:
    name = None  # type: str
    gender = None  # type: str
    #  私有成员用__前缀定义，外围无法使用
    __age = None
    frequency: int = 0
    duration: int = 0

    # 构造方法
    def __init__(self, name):
        self.name = name
        print(f"创建了一个构造方法，名字={name}")

    # __功能__ 方法重写，除了str还可以定义lt,gt,eq
    def __str__(self):
        return f"name={self.name}"

    # def say_hi(self):
    #     # 访问内部元素，需要加self访问
    #     print(f"Hello {self.name}")

    # 同名方法会做覆盖，后面的会覆盖前面的
    def say_hi(self, msg):
        # 访问内部元素，需要加self访问
        print(f"Hello {self.name}", msg)

    # 定义一个闹钟
    def ring(self):
        import winsound
        winsound.Beep(self.frequency, self.duration)


name = "张惠"
stu = Student(name)
# stu.say_hi()
stu.name = "Ask"
stu.say_hi("今天天气好")
stu.frequency = 2000
stu.duration = 1000
# stu.ring()
print(stu)
