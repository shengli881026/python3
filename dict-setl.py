#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python 如果需要print打印中文需要在开头设置utf-8编码格式,

'''
    raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
	而对于 input() ，它希望能够读取一个合法的 python 表达式，
	即你输入字符串的时候必须使用引号将它括起来，
	否则它会引发一个 SyntaxError 。
	raw_input() 将所有输入作为字符串看待，返回字符串类型。
	而 input() 在对待纯数字输入时具有自己的特性，
	它返回所输入的数字的类型（ int, float ）；同时在例子 1 知道，
	input() 可接受合法的 python 表达式，举例：input( 1 + 3 ) 会返回 int 型的 4
'''

# 接受用户数据的年龄,来判断当前处于哪个年龄段
name = input("请输入需要查询成绩学生的姓名:")

# print type(name) 获取输入的类型

d={'zhangsan':100,'lisi':87,'wangwu':91,'zhaoliu':61}

d['heiqi'] = d['libaiyi'] = d['beisailei'] = d['ali']=71

#print d



def get_chengji(name,d):
	if (name in d):
		return d[name]
	else:
		return 0
	
chengji = get_chengji(name,d)
print ('查询到的成绩为:'+str(chengji))