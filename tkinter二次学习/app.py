#1、图形化界面设计的基本理解
#导入 tkinter 模块
#创建 GUI 根窗体
#添加人机交互控件并编写相应的函数。
#在主事件循环中等待用户触发事件响应。
from tkinter import *
root= Tk()
root.title('第一个Python窗体')
root.geometry('240x340') # 这里的乘号不是 * ，而是小写英文字母 x
root.mainloop()
