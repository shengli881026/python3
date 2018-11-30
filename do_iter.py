import os
'''
* python list - 列表生成式
* 列表生成式是Python内置的非常简单却强大的可以用来创建list的生成式，也就是通过特定的表达式来生成特定的list
'''
'''
# 生成 1x1、2x2、 3x3、4x4、5x5 这样特定格式的一组list 
# 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
'''
n_list = [ x * x for x in range(1,11)]
print(n_list)

new_list = [ x* x for x in range(1,11) if x % 2 == 0]
print(new_list)
dir_list  = [ d for d in os.listdir('../../mob/app/mapi/v4')]

# 文件的操作；open 返回的是一个 file 的对象
f = open('../mob-api.php','r',encoding='UTF-8')
#print(f.read())
f.close()
print(dir_list)

# 使用内建的isinstance函数可以判断一个变量是不是字符串：

nn = 33

def is_str(nn):
    if(isinstance(nn,str) == True):
        return '是字符串'
    else:
        return '不是字符串'

print(is_str(nn))