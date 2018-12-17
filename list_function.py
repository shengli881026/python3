'''
 * list 是一种有序的集合列表 在这里介绍list 列表相关的操作方法
'''

# 对字符串 进行切片成list
h_list = list("hello word")
#print(h_list)
# 对切片后的list 进行赋值操作，h_list[4:] 通过list 另外一个切片的数据替换h_list 下标4-最后的
h_list[4:5] = list("skwnwnwnw")
#print(h_list)

#=====================================list 列表的相关的函数操作=============================================
# 操作list 的增删改
names_list = ['zhangsan','lisi','wangwu','zhaoliu']
#在name_list 的末尾增加一个元素到列表中
names_list.append("wangbaqi")
print("append 函数追加元素到list 末尾: " + str(names_list) )
# 如何删除一个元素呢？使用del list[0]命令
del names_list[0]
new_name_list = names_list.copy()
print(new_name_list)
print("count 方法的使用" + str(new_name_list.count('lisi')))
#  clear 方法用于清空列表
names_list.clear()
print("clear 方法的使用：" + str(names_list))


# 切片复制的操作
a_w = list("zhangsan")
# 切片后进行赋值操作
a_w[5:] = list("xiao")
print(a_w)






