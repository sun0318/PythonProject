import tkinter as tk

def press_key(key):
    if key == '=':
        try:
            result = eval(display.get())
            display.delete(0, tk.END)
            display.insert(tk.END, result)
        except Exception as e:
            display.delete(0, tk.END)
            display.insert(tk.END, "Error")
    elif key == 'C':
        display.delete(0, tk.END)
    else:
        display.insert(tk.END, key)

# 创建主窗口
root = tk.Tk()
root.title("Calculator")

# 创建显示框
display = tk.Entry(root, width=25, font=('Arial', 14), justify=tk.RIGHT)
display.grid(row=0, column=0, columnspan=4)

# 创建按钮
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C'
]

row = 1
col = 0
for button in buttons:
    tk.Button(root, text=button, width=5, height=2,
              command=lambda b=button: press_key(b)).grid(row=row, column=col)
    col += 1
    if col > 3:
        col = 0
        row += 1

# 运行主循环
root.mainloop()

if __name__ == "__main__":
    print("aaa")