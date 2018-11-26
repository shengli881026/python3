#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式,


d={'zhangsan':100,'lisi':87,'wangwu':91,'zhaoliu':61}

# 获取 d 元组中key 的值
for key1 in d:
	print (key1)

# 获取 tuple元组中 结构中数据，key和value
for key,val in d.items():
	print (key+'---'+str(val))

