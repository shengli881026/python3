#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式

def trim(s):
	#对字符串进行切片处理
	cont = ''
	sr = ''
	if(s[0:1] ==' '):
		#print(s[1:])
		sr = s[1:]
		cont = cont +"字符串开头有空格"
	else:
		sr = s
		cont = cont +"开头无空格"
	# 出来末尾空格
	l = len(sr)
	if(sr[-1] ==' '):
		sr = sr[0:l-1]
		cont = cont+"----字符串末尾有空格"
	else:
		cont = cont +"*****末尾无空格"

	return (sr,cont)
		
x,y = trim(" hello sss")

print (x + '---'+str(y))