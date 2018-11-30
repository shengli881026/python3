'''
# map/reduce  高进阶函数
#
'''
# 定义list
num_list =  [ j for j in range(1,11)]
print(num_list)
def func(x):
    return x * x

'''
 # map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
'''
func_num = map(func,num_list)
print(func_num,list(func_num))
