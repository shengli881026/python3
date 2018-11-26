#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式,

'''
	自定义 def 函数 来计算;
'''
def get_nums(i):
	if(i > 0):
		return i
	else:
		return -i


def return_args(j,k):
	m = j+k
	n = j*k
	return m,n



print ("输出:"+str(get_nums(10)))

u,v = return_args(2,3)
print ("两个数相加="+str(u)+"，相乘="+str(v))