import threading
import time

def task():
    sema.acquire()
    time.sleep(1)
    obj = threading.current_thread()
    print("当前是线程[{0}],已经开始运行了...".format(obj.getName()))
    sema.release()


if __name__ == '__main__':

    sema = threading.Semaphore(3)  # 实例化信号量锁对象,代表每次都跑3条。

    for i in range(10):
        t1 = threading.Thread(target=task,)  # 开启10条线程
        t1.start()  # 等待CPU调度执行



# ==== 执行结果 ====

"""
当前是线程[Thread-1],已经开始运行了...
当前是线程[Thread-3],已经开始运行了...
当前是线程[Thread-2],已经开始运行了...

当前是线程[Thread-4],已经开始运行了...
当前是线程[Thread-6],已经开始运行了...
当前是线程[Thread-5],已经开始运行了...

当前是线程[Thread-7],已经开始运行了...
当前是线程[Thread-9],已经开始运行了...
当前是线程[Thread-8],已经开始运行了...

当前是线程[Thread-10],已经开始运行了...
"""
