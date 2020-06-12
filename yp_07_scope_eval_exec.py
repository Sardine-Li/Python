scope = {}
exec("a1 = 5", scope)
exec("a2 = 10", scope)
exec("a3,a4 = 15,20", scope)
for num1 in range(1,5):
    value1 = scope['a' + str(num1)]
    print( "a%s : %s" % (num1,value1))
# exec(): 执行一个语句，不可以是字符串表达式？

b1 = "nihao"
b2 = "石头"
b3 = 150
for num2 in range(1,4):
   value2 = eval('b' + str(num2))
   print("b%s : %s" % (num2,value2))
# eval(): 函数用来执行一个字符串表达式，并返回表达式的值。

from math import sqrt
scope = {}
exec('sqrt = 2.57', scope)
print(sqrt(4))
print(scope['sqrt'])
print(type(sqrt))

#给exec或者eval提供命名空间时，还可以在真正使用命令空间前放置一些值(字符串也可)进去：
scope = {}
scope['c1'] = "石头"
scope['c2'] = "剪刀"
for num3 in range(1,3):
    value3 = scope['c' + str(num3)]
    print( "c%s : %s" % (num3,value3))

#exec或者eval调用的作用域也能在另外一个上面使用：
scope = {}
exec('x = 4', scope)
print(eval('x * x', scope))


# eval:计算字符串中的表达式
# exec:执行字符串中的语句
# execfile:用来执行一个文件