#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
# if 语句的使用， if，else if , elif,else 共有四种if 判断语法。
# if语句执行有个特点，它是从上往下判断，如果在某个判断上是True，把该判断对应的语句执行后，就忽略掉剩下的elif和else。
#
'''

# 接受用户数据的年龄,来判断当前处于哪个年龄段
age_numbser = int(input("请输入你的年龄并按回车键确认....."))

print age_numbser

# 
# 定义一个年龄判断的方法，判断输入的年龄是属于什么阶段<少年、青年、成年、中年、老年>
#

age_name = ['婴儿期','幼儿期','儿童期','少儿期','青年期','成年期','老年期','高龄器','长寿期','妖怪'];

'''
	根据年龄判断年龄段
'''
def check_age(age):
	if (age >0 and age <= 3):
		return 1
	elif (age >3 and age <= 6):
		return 2
	elif (age >6 and age <= 12):
		return 3
	elif (age >12 and age <= 15):
		return 4
	elif (age >15 and age <= 25):
		return 5
	elif (age >25 and age <= 60):
		return 6
	elif (age >60 and age <= 79):
		return 7
	elif (age >79 and age <= 89):
		return 8
	elif (age >89 and age <= 120):
		return 9
	else :
		return 10

#获取当前年龄所处的年龄段
print age_name[check_age(age_numbser)-1];



