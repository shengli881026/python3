#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
 @author zhangshengli
'''
# for 语句遍历list 

user_name = ['zhangsan','lisi','mac','cuirui','liqi','hongjia','beipo']

for name in user_name:
	print "用户名:"+name+"\r";

nums = list(range(1,101))


def get_sum_num(num_list):
	n =0
	if(len(num_list) > 0):
		for x in num_list:
			n = n + x
		return  n
	else:
		return 0

sum_num = get_sum_num(nums)
print sum_num
#print "汇总的结果为:"+ sum_num


'''
  计算100以内的偶数之和
'''

def sum_even():
	sum_n = 0
	n = 100
	while n > 0:
		sum_n = sum_n+n 
		n = n-2
	return sum_n


def func_break():
	m = 1
	while m  <= 100:
		if(m > 50):
			break
		elif m == 10:
			continue
		print(m)
		m = m+1


print sum_even();

func_break();