import threading


def task():
    obj = threading.current_thread()
    print("当前是线程[{0}],已经开始运行了...".format(obj.getName()))
    print("当前是线程[{0}],红灯了，停车...".format(obj.getName()))
    event.wait()  # 暂停，等待绿灯通行
    print("当前是线程[{0}],绿灯了放行...".format(obj.getName()))
    print("当前是线程[{0}],卧槽怎么又是红灯，停车...".format(obj.getName()))
    event.wait()  # 暂停，等待绿灯通行
    print("当前是线程[{0}],继续运行...".format(obj.getName()))


if __name__ == '__main__':

    event = threading.Event()  # 实例化事件锁对象

    for i in range(10):
        t1 = threading.Thread(target=task,)  # 开启10条线程
        t1.start()  # 等待CPU调度执行

    event.set()  # 设置为绿灯 针对第一次
    event.clear()  # 设置为红灯，如果没有他那么上面不管wait()多少次都没用了。因为全都是绿灯
    event.set()  # 再次设置为绿灯，针对第二次


# ==== 执行结果 ====

"""
当前是线程[Thread-1],已经开始运行了...
当前是线程[Thread-1],红灯了，停车...
当前是线程[Thread-2],已经开始运行了...
当前是线程[Thread-2],红灯了，停车...
当前是线程[Thread-3],已经开始运行了...
当前是线程[Thread-3],红灯了，停车...
当前是线程[Thread-4],已经开始运行了...
当前是线程[Thread-4],红灯了，停车...
当前是线程[Thread-5],已经开始运行了...
当前是线程[Thread-5],红灯了，停车...
当前是线程[Thread-6],已经开始运行了...
当前是线程[Thread-6],红灯了，停车...
当前是线程[Thread-7],已经开始运行了...
当前是线程[Thread-7],红灯了，停车...
当前是线程[Thread-8],已经开始运行了...
当前是线程[Thread-8],红灯了，停车...
当前是线程[Thread-9],已经开始运行了...
当前是线程[Thread-9],红灯了，停车...
当前是线程[Thread-10],已经开始运行了...
当前是线程[Thread-10],红灯了，停车...
当前是线程[Thread-10],绿灯了放行...
当前是线程[Thread-10],卧槽怎么又是红灯，停车...
当前是线程[Thread-5],绿灯了放行...
当前是线程[Thread-9],绿灯了放行...
当前是线程[Thread-9],卧槽怎么又是红灯，停车...
当前是线程[Thread-1],绿灯了放行...
当前是线程[Thread-1],卧槽怎么又是红灯，停车...
当前是线程[Thread-6],绿灯了放行...
当前是线程[Thread-6],卧槽怎么又是红灯，停车...
当前是线程[Thread-3],绿灯了放行...
当前是线程[Thread-4],绿灯了放行...
当前是线程[Thread-2],绿灯了放行...
当前是线程[Thread-1],继续运行...
当前是线程[Thread-5],卧槽怎么又是红灯，停车...
当前是线程[Thread-3],卧槽怎么又是红灯，停车...
当前是线程[Thread-7],绿灯了放行...
当前是线程[Thread-7],卧槽怎么又是红灯，停车...
当前是线程[Thread-7],继续运行...
当前是线程[Thread-4],卧槽怎么又是红灯，停车...
当前是线程[Thread-3],继续运行...
当前是线程[Thread-10],继续运行...
当前是线程[Thread-5],继续运行...
当前是线程[Thread-8],绿灯了放行...
当前是线程[Thread-6],继续运行...
当前是线程[Thread-4],继续运行...
"""
