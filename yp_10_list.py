name_list = ["liyanping", "liuxiulian", "lizhiyu"]
num_list = [5, 8, 9, 3 ,4, 2, 7, 14]

# 1.取值和取索引
print(name_list[1])
print(name_list.index("lizhiyu"))

# 2.修改
name_list[2] = "lizhiyu01"
# 直接定义特定索引序号的内容进行修改

# 3.增加
name_list.append("lizhiyu02")
name_list.insert(2, "lizhiyu03")
temp_list = ["nihao", "hello_world"]
name_list.extend(temp_list)
# 定义临时列表，并将其扩展添加至某一列表

# 4.删除
name_list.remove("lizhiyu03")
# remove删除指定内容,若有多个同名元素，默认删除第一次出现的元素
name_list.pop()
# pop删除指定索引号的内容，默认删除最后一个元素
name_list.pop(3)
# name_list.clear()

del name_list[3]
# del关键字将变量从内存中删除，后续代码无法使用该删除的变量

list_len = len(name_list)
print(list_len)

count = name_list.count("liyanping")
print(count)

# num_list.sort()
num_list.sort(reverse = True)
# num_list.reverse()

print(num_list)
print(name_list)

for my_name in name_list:
    print("我的名字叫 %s" % my_name)
# for in：从对象中依次获取所有元素
