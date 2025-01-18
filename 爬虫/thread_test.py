from time import time
from time import sleep
from multiprocessing.dummy import Pool
def get_info(parm):
    print(parm+'开始下载')
    sleep(2)
    print('下载结束！！！')
    return 1

str_list = ['a','b','c']
start_time = time()
# for i in str_list:
#     get_info()

pool = Pool(3)
a = pool.map(get_info,str_list)
end_time = time()
print(end_time-start_time)
print(sum(a))