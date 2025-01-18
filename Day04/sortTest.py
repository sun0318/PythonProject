# my_list = ["3","4","5","1","2"]
#
# my_list.sort(reverse=True)
# print(my_list)
# 定义一个函数供sort调用，返回需要参考排序元素的值的位置
def find_sort_key(element):
    return element[0]

mylist = [["1","4","5","1","2"],["3","4","5","1","2"],["2","4","5","1","2"]]
# 数组做排序，控制按数组的第几个元素排序，key值是函数名，函数名后面不要加()。
mylist.sort(key=find_sort_key, reverse=True)
print(mylist)