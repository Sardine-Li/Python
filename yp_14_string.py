str1 = "我的外号是'燕平'"

print(str1.count("号"))

print(len(str1))

print(str1[3])

print(str1.index("外号"))

print(str1)

# 判断空白字符（转义字符属于空白字符）
space_str = " \r \n \t"
print(space_str.isspace())
print(space_str.isspace)

# 判断字符串是否只包含数字
num_str = "十一"
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
# isnumeric可以判断中文数字

print(str1.startswith("我"))
print(str1.endswith("'燕平'"))
print(str1.find("外号"))
print(str1.find("小号"))
# find方法指定字符串不存在会返回-1，index则会报错，无法执行

print(str1.replace("外号", "小号"))
# replace方法执行完之后会返回新的字符串内容，但是，原字符串不会被修改

str2 = "  nihaoa  "
print(str2.lstrip())
print(str2.rstrip())
print(str2.strip())
# 去除空白字符，包含转义字符

# 字符的拆分与连接
str3 = "今晚\t 夜色\t \n 真美！"
print(str3)
str3_list = str3.split()
print(str3_list)

print( " ".join(str3_list))
# 以空格为连接符，连接列表的所有内容为一个新的字符串

num_str1 = "0123456789"

print(num_str1[2:6])
# 截取数字2~5

print(num_str1[2:])
# 截取2到末尾的数字

print(num_str1[:])
# 截取出所有内容

print(num_str1[::2])
# 从开始位置，到结束，每隔一个步长（步长为2）截取一个字符

print(num_str1[1::2])
# 从索引1（第二个字符）位置开始，到结束，每隔一个步长（步长为2）截取一个字符

print(num_str1[2:-1])
# 从索引2（第三个字符）位置开始，到末尾倒数第二个字符

print(num_str1[-2:])
# 从字符串末尾的两个字符

# 将字符串倒序输出
num_str1_len = len(num_str1)
num_str1_list = []
for str1_num in range(num_str1_len):
    num_str1_list_temp = [num_str1[str1_num:str1_num + 1]]
    num_str1_list.extend(num_str1_list_temp)
num_str1_list.sort(reverse = True)
print(num_str1_list)
print( "".join(num_str1_list))

print(num_str1[-1::-1])
print(num_str1[::-1])
