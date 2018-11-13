#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式,


'''
	* 函数的参数 Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，
	* 使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码。
	* 1、位置参数 2、默认参数 3、可变参数 4、关键字参数 5、命名关键字参数 6、参数组合
	*
	* 
'''
#-----------------------------------位置参数-------------------------------------
# 1、位置参数
# 计算一个数x，连续乘以y次的数值，数值的N次方
def power(x,y):
	s =1
	while y > 0:
		y = y-1
		s = s * x
	return s
	
print "位置参数-例子1- 结果"+str(power(2,3))
#-----------------------------------位置参数-------------------------------------



#-----------------------------------默认参数--------------------------------------

# 计算一个数相加的结果

def getNum(a,b = 0):
	return a+b

print "默认参数-1 - 结果"+str(getNum(2))

'''
从上面的例子可以看出，默认参数可以简化函数的调用。设置默认参数时，有几点要注意：

一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；

二是如何设置默认参数。

当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

使用默认参数有什么好处？最大的好处是能降低调用函数的难度。
默认参数降低了函数调用的难度，而一旦需要更复杂的调用时，又可以传递更多的参数来实现。
无论是简单调用还是复杂调用，函数只需要定义一个。

'''

def addUser(user_id,user_name,user_age = 10,city_name='beijing'):
	print "默认参数-例子2-"+str(user_id)+'-'+ str(user_name) +'-'+str(user_age)+'-'+ str(city_name)

# 写法一：按照顺序填充
addUser(1,'zhangsan');
# 写法二：根据变量可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
addUser(2,'zhangsan',city_name='shanghai');
#写法三：可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上，可以进行相互的交叉
addUser(3,'zhangsan',city_name='shanghai',user_age='23');

#-----------------------------------默认参数--------------------------------------


#-----------------------------------可变参数--------------------------------------
'''
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
'''
def getnumbsers(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
		print "位置参数-例子1- 结果"+str(sum)

#第一种调用形式
getnumbsers(1,2,4,5,6,7,8,9)
#第二种调用形式
s_n = [8,9,11,12]
getnumbsers(s_n[0],s_n[1],s_n[2],s_n[3])
#第三种调用形式
getnumbsers(*s_n)
#-----------------------------------可变参数--------------------------------------


#-----------------------------------关键字参数--------------------------------------
# 说明 (**args) 关键字参数允许你传入0个或任意个含参数名的参数，
# 这些关键字参数在函数内部自动组装为一个dict 字典类型的结构 - 使用键-值（key-value）存储，具有极快的查找速度。
def test1(name,city,**args):
    print('name:', name, 'city:', city, 'args:', args)
#比如，在test1函数里，我们保证能接收到name和city这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到;
# 第一种写法,args 接受的是一种赋值参数
test1('zhangsan','beijng',city_id=20,nums='1000')
# 第二种写法，args 接受的是一个 dict字典中的键值对数据；然后在函数调用时就需要赋值
#也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
args_dict = {'weixin_id':'100','weixin_name':'xxxloo','city_id':'20'}
test1('lisi','hangzhou',weixin_id=args_dict['weixin_id'],weixin_name=args_dict['weixin_name'])
# 第三种写法
# **args_dict表示把args_dict这个dict的所有key-value用关键字参数传入到函数的**args参数，
# args将获得一个dict，注意args获得的dict是args_dict的一份拷贝，对args的改动不会影响到函数外的args_dict。
test1('wangwu','shanghai',**args_dict)


#-----------------------------------关键字参数--------------------------------------

#-----------------------------------命名关键字参数--------------------------------------
#传入params 函数的调用者可以传入任意不受限制的关键字参数params ,然后在函数内验证参数
def setParams(i_d,name,**params):
	if 'city' in params:
		print "检查到city 参数"+str(params['city'])
		pass
	if 'weixin_id' in params:
		print "检查到weixin_id 参数"+str(params['weixin_id'])
		pass
	print '命名关键字参数' + str(('i_d',i_d,'name',name,'params',params))

setParams(2891,'louuw',city='beijing',weixin_id=9922)

# 关键字参数，限制关键字参数的名字,就可以用命名关键字参数,例如，上面的setParams 只接受city,weixin_id
#def setParams2(i_d,name,*,city,weixin_id):
#	print ('i_d',i_d,'name',name,'city',city,'weixin_id',weixin_id)
#和关键字参数**params不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
#setParams2(1020,'popwqq',city='hangzhou',weixin_id=8381)

#def person(name, age, *args, city, job):
#    print(name, age, args, city, job)

#person('Jack', 24, 'Beijing', 'Engineer')




#-----------------------------------参数组合--------------------------------------
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
'''



#------------------------------------遗留的问题-----------------------------------
# 问题1、python 的默认参数为什么不能放到前面，里面下面的abc方法，运行abc 会报错
# SyntaxError: non-default argument follows default argument
'''
def abc(a=1,b):
	#print a
aaa(1,3);
'''

