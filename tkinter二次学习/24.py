import tkinter as tk

app = tk.Tk()
app.title("FishC Demo")
#标签控件；可以显示文本和位图
theLable = tk.Label(app, text="你若安好，便是晴天",width=20,height=10)
theLable.pack()

app.mainloop()
