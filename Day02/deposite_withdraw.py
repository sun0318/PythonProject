balance = 0
name = None
# name = input("请输入您的名字:")


def menu():
    print(f"{name}，您好，欢迎来到招商银行，请选择操作")
    print("查询余额\t【输入1】")
    print("存款\t\t【输入2】")
    print("取款\t\t【输入3】")
    print("退出\t\t【输入4】")
    print("请输入你的选择")
    return input()


def withdraw(money :int) -> None:
    print(f"{name}，您好，您取款{money}元成功")
    global balance
    balance -= money
    print(f"{name}，您好，您的余额剩余：{balance}元")


def deposit(money):
    print(f"{name}，您好，您存款{money}元成功")
    global balance
    balance += money
    print(f"{name}，您好，您的余额剩为：{balance}元")


def querybalance():
    print("-------------------查询余额-------------------")
    print(f"{name}，您好，您的余额剩余：{balance}元")


while True:
    operation = menu()
    if operation == "1":
        querybalance()
        continue
    elif operation == "2":
        money = input("请输入您要存款的金额:")
        deposit(int(money))
        continue
    elif operation == "3":
        money = input("请输入您要取款的金额:")
        withdraw(int(money))
        continue
    else:
        print("已退出")
        break
