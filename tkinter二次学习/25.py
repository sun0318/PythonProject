import tkinter as tk
class App: #定义类
    
    def __init__(self, master):
        frame = tk.Frame(master)#定义窗体框架
        frame.pack(side=tk.RIGHT, padx=100,pady=100)
        
        #定义按钮
        self.hi_there = tk.Button(frame, text="打招呼",bg="red" ,fg='green',command=self.say_hi)
        self.hi_there.pack(padx=10, pady=10)#位置
        
    def say_hi(self):
        print("嗨，好久不见，你可安好！")
             
root = tk.Tk()
app = App(root)
root.mainloop()
