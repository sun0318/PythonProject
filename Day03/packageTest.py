# import模块名
# import time
# from：导入模块里的方法，直接调方法
# from 模块名 import 功能名
# from time import sleep
# from 模块名 import *
# from time import *
# as定义别名
# import time as tt
# import testFunction
# 当导入多个模块的时候，且模块内有同名功能. 当调用这个同名功能的时候，调用到的是后面导入的模块的功能
from testFunction import *
# import testFunction
# sleep(1)
# tt.sleep(1)
add(1,2)
# minus(1,2)

# 调用其他包里的类
from Day02 import *
demo2.fun1("测试")

# __all__针对的是 ’ from ... import * ‘ 这种方式
# 对 ‘ import xxx ’和 from ... import 具体名称 ‘ 这种方式无效
# from Day04 import *
# test1.fun1()

#  安装第三方包
#  在cmd里执行命令 pip install 包名称
#  pip install numpy
