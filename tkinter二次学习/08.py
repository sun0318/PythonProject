#方法二：利用textvariable变量属性来实现文本变化。
import tkinter
import time

def gettime():
      var.set(time.strftime("%H:%M:%S"))   # 获取当前时间
      root.after(1000,gettime)   # 每隔1s调用函数 gettime 自身获取时间

root = tkinter.Tk()
root.title('时钟')
var=tkinter.StringVar()

lb = tkinter.Label(root,textvariable=var,fg='blue',font=("黑体",80))
lb.pack()
gettime()
root.mainloop()
