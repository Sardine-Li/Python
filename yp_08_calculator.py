def calculator1():
    num1 = float(input("请输入要相加的第一个数字：\n"))
    num2 = float(input("请输入要相加的第二个数字：\n"))
    print("两个数字的和为：%s + %s = %s" % (num1, num2, (num1 + num2)))
    # 将要打印输出的数值转换为字符串，规避显示精度及后缀0的问题

# calculator1()


def calculator2(num3, num4):
    # num3 = float(input("请输入要相加的第一个数字：\n"))
    # num4 = float(input("请输入要相加的第二个数字：\n"))
    print("两个数字的和为：%s + %s = %s" % (num3, num4, (num3 + num4)))
    # 将要打印输出的数值转换为字符串，规避显示精度及后缀0的问题

calculator2(2.56, 3.14)
# 给函数赋予参数，调用的时候直接输入参数进行执行


from decimal import Decimal
# 引入Decimal确认高精度计算

def calculator3(num5, num6):
    # num3 = float(input("请输入要相加的第一个数字：\n"))
    # num4 = float(input("请输入要相加的第二个数字：\n"))
    print("两个数字的和为：%s + %s = %s" % (num5, num6, (num5 + num6)))
    print("两个数字的和为：%s + %s = %s" % (Decimal(num5), Decimal(num6), (Decimal(num5) + Decimal(num6))))
    # 将要打印输出的数值转换为字符串，规避显示精度及后缀0的问题

calculator3(2.56, 3.14)

str1 = "     this is string example....wow!!!     "
print(str1.rstrip())
str2 = "88888888this is string example....wow!!!8888888"
print(str2.rstrip('8'))