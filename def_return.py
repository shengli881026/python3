'''
python def 函数中返回值的实例：
'''

'''
 def 函数中如果 return  这样的返回值是None 
 None 是Python的特殊类型，Null对象或者是None Type，它只有一个值None.
'''
def abc(w):
    return

print(abc(2))# 返回值None

# 定义一个函数,没有返回值
def getNun(x):
    y = x + 1

'''
此时返回值为 None
None 是Python的特殊类型，Null对象或者是None Type，它只有一个值None.
if X is None; 来判断是否为None 
'''
print(getNun(2))

def getNumF(y):
    q = y * 10
    return q > 20

print(getNumF(3))


