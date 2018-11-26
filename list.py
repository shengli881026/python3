#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# list 是一种有序的集合，可以随时添加和删除其中的元素。
# tuple 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改。
# list和tuple是Python内置的有序集合，一个可变，一个不可变。根据需要来选择使用它们。
#

# 定义一个list,记录用户名
list_user = ['zhangsan','lisi',['qiba','liusiwu','qiwanglei'],'wangwu','zhaoliu']
#获取list_user 的list 长度
len_list_user = len(list_user)
# list_user[3] 也可以通过索引下表获取元素

# 定义一个函数来获取用户名
def get_user_name(i):
	if(i-1 <=len_list_user):
		return list_user[i-1]
	else:
		return '没有此用户'

# 
# 添加用户，在list的指定位置，添加
#
def add_user_name(name,j=0):
	list_user.insert(j,name)

# 删除用户,list_user 删除元素
def del_user_name(k=0):
	if(k > 0 ):
		list_user.pop(k)
	else:
		# 默认从末尾删除
		list_user.pop();

# 在list 的末尾追加元素
list_user.append('Adam')
# 在list开头位置追加元素
add_user_name('niuren')
# 在指定的位置添加元素
add_user_name('meituan',3)
print (list_user)
# 删除元素
del_user_name()
print (list_user)
del_user_name(4)
print (list_user)

print (get_user_name(5))


# tuple元组 

cat_user_name = ('yiqu','wangq','lpeoww',['niw','soql'])

print (cat_user_name)

