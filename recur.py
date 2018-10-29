#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式,



def fact_iter(num,nk):
	if num == 1:
		return nk
	return fact_iter(num-1,num*nk)

#3,20


def move_abc(n,a,b,c):
	if n==1:
		print(a,'--->',c)


move_abc(3,'A','B','C')
#print fact_iter(4,5)



