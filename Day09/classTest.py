def func1():
    test = myClass()
    test.my_run()

class myClass:
    def __init__(self):
        print('初始化')

    def my_run(self):
        i = 's'
        # globals()[f'data_{i}'] = 666
        locals()['data_s'] = 666
        if i == 's':
            print(data_s)
            print(globals()['data_s'])
            print(dir())

func1()
