print("Hello Python!")
#print("Hello Python1!")
#print("Hello Python2!")
'''
qq_number = '1156169001'
print(qq_number)
'''
#'''
#price = 10
print('开业大酬宾，"苹果"满10减5！')
#price_str = input("请输入苹果的价格\n")
price = float(input("请输入苹果的价格\n"))
#print(price)
#weigth = 0.8
#weigth_str = input("请输入苹果的重量\n")
weigth = float(input("请输入苹果的重量\n"))
#print(weigth)
money = price * weigth
if money >= 10:
    money = money -5
else:
    pass
print(money)
from decimal import Decimal
#money = str(money)
money1 = Decimal(money).quantize(Decimal("0.00"))
print(money1)
print("%.2f" % money)
#'''
'''
name = '小明'
age = '18'
sex = '男'
height = '175cm'
weigth = '65kg'
print('姓名 = ', name)
print('年龄 = ', age, '岁')
'''
'''
import random
a = random.randint(0,100)
b = random.randint(0,100)
print(a*b) 
print(type(a))
'''

# >>> from decimal import Decimal
# >>> from fractions import Fraction
# fractions 模块支持分数运算。
# float.as_integer_ratio() 方法会将浮点数表示为一个分数

# >>> Fraction.from_float(0.1)
# Fraction(3602879701896397, 36028797018963968)

# >>> (0.1).as_integer_ratio()
# (3602879701896397, 36028797018963968)

# >>> Decimal.from_float(0.1)
# Decimal('0.1000000000000000055511151231257827021181583404541015625')

# >>> format(Decimal.from_float(0.1), '.17')
# '0.10000000000000001'
