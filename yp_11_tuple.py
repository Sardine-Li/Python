info_tuple = ("liyanping", 28, 1.70)
single_tuple = ("liuxiulian",)
empty_tuple = ()

num_list = [5, 8, 9, 3 ,4, 2, 7, 14]

print(type(info_tuple))
print(type(single_tuple))
print(type(empty_tuple))

print(info_tuple[0])

print(info_tuple.index("liyanping"))
print(info_tuple.count(28))

for item in info_tuple:
    print(item)

print("%s的年龄是%d岁，身高是%.2fm" % info_tuple)

info_str = ("%s的年龄是%d岁，身高是%.2fm" % info_tuple)
# 用元组拼接新的字符串
print(info_str)

num_tuple = tuple(num_list)
print(type(num_tuple))

info_list = list(info_tuple)
print(type(info_list))

