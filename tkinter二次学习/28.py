import threading

num = 0
def add():
    lock.acquire()  # 上锁 + 1
    lock.acquire()  # 上锁 + 1
    global num
    for i in range(10000000):  # 一千万次
        num += 1
    lock.release()  # 解锁 - 1
    lock.release()  # 解锁 - 1

def sub():
    lock.acquire()  # 上锁
    lock.acquire()  # 死锁
    global num
    for i in range(10000000):  # 一千万次
        num -= 1
    lock.release()  # 解锁 - 1
    lock.release()  # 解锁 - 1

if __name__ == '__main__':

    lock = threading.RLock()  # 实例化递归锁对象

    t1 = threading.Thread(target=add,)
    t2 = threading.Thread(target=sub,)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("最终结果:",num)

# ==== 执行结果 ==== 三次采集

"""
最终结果: 0
最终结果: 0
最终结果: 0
"""
