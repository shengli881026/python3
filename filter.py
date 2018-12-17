'''
 - python 内置的 filter 函数用于过滤数据处理
 - 过滤list 或者 map 等数据结构
'''

''' 
    使用filter 过滤list 数据 和PHP的 array_filter 数据函数有点类似
'''
# 计算list 中的偶数
def getQ(num):
    if(num % 2 == 1):
        return True
    else :
        return False
obj = filter(getQ,[1,2,3,4,5,6,7,8,9,10,11,12])
print(list(obj))

# 检查一个list中，那个元素是纯数字
n_list = ['zhang sss','leism','9391','9192','skeiw','213','483','ss381']


