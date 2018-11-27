'''
***  python 的列表 list 和有序列表（元组）tuple 的切片操作
***  通过例子来演示如何对list 和tuple 进行切片；
'''

user_name = ['zhangsan','lisi','wangwu','zhaoliu','liqi','maba','zhaojiu','xiliu','qiqi']

print('获取用户列表中前四个用户，相当于PHP 数组中的array_slice | user_name[0:4] = ',user_name[0:4])
print('获取用户列表中前3个用户 | user_name[:3] = ',user_name[:3])
print('获取用户列表中最后一个用户 | user_name[-1:] = ',user_name[-1:])
print('获取用户列表中最后两个用户 | user_name[-2:] = ',user_name[-2:])
print('获取用户列表中第3，5个用户 | user_name[3:5] = ',user_name[3:5])

rang_list = list(range(1,101))
print("获取前十个数",rang_list[:10])
print("获取后十个数",rang_list[-10:])
# -3 代表获取list 最后第三个数是什么，-3: 代表后三个数是什么，是一个list
print("获取最后第三个数",rang_list[-3])
print("获取10-20个数",rang_list[10:20])
print("前10个数，每两个取一个：",rang_list[:30:2])
print("所有数，每5个取一个：",rang_list[::5])
# [:]就可以原样复制一个list：
new_rang_list = rang_list[:]
print(new_rang_list)
tuple_list = ('a','b','c','d','e','f','h')
print(tuple_list[3:])