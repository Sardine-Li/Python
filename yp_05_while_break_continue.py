#while循环练习
i = 0
while i <= 3:
    print(i)
    i = i + 1
print("循环结束后，i = %d" % i)

print("求1至100的算术和")
num = 0
value = 0
while num <= 100:
    if num == 99:
        num +=1
        continue
    value = value + num
    num +=1
print("num = %d" % num)
print("总和 = %d" % value)
# continue:跳过while语句段中continue后面的所有语句，回到while条件判断重新开始执行
# continue后面要加计数器语句，防止死循环

j = 0
while j <= 10:
    print(j)
    if j == 3:
        break
    j = j + 1
print("循环结束后，j = %d" % j)
# break:跳过while语句段中break后面的所有语句，同时跳出整个while循环