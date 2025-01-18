def outter(origin):
    # print(1111)
    def inner():
        print("before")
        res = origin()
        print("after")
        print(res)
        return res
    return inner

# 运行时，已经加载过了，会输出111，此时的func其实就是outter里面的inner函数
@outter
def func():
    print("这里是func函数")
    return 1

func()

# func = outter(func)