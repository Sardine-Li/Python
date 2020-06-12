print('Hello Python')
# print('Hello Python1')
# print('Hello Python2')
#石头剪刀布游戏

print("我们来开始石头剪刀布游戏吧！")

str1 = "石头"
str2 = "剪刀"
str3 = "布"

import random
type_machine_int = random.randint(1,3)
# 通过调用随机函数让电脑随机出手型

"""
type_human = (input("请输入你要出的手型（石头/剪刀/布）：\n"))
if type_human != str1 and type_human != str2 and type_human != str3 :
    print("需要输入正确的手型（石头/剪刀/布）^_^")
    type_human = (input("请再次输入你要出的手型：\n"))
    if type_human != str1 and type_human != str2 and type_human != str3 :
        print("你还是输错了，游戏结束了^_^")
    else:
        pass
else:
    pass
# 人工直接输入手型描述文字进行游戏

if type_human == str1:
    type_human_int =1
elif type_human == str2:
    type_human_int =2
else:
    type_human_int =3
# 将人的手型转换为数值，是否可以通过查表来实现而不是if循环？
"""

type_human_int = int(input("请输入你要出的手型数字-石头(1)/剪刀(2)/布(3)：\n"))
if type_human_int != 1 and type_human_int != 2 and type_human_int != 3 :
    print("需要输入正确的手型数字^_^")
    type_human_int = (input("请再次输入你要出的手型数字-石头(1)/剪刀(2)/布(3)：\n"))
    if type_human_int != 1 and type_human_int != 2 and type_human_int != 3 :
        print("你还是输错了，游戏结束了^_^")
    else:
        pass
else:
    pass
# 通过键盘输入人出的手型

type_machine1 = type_human1 = str1
type_machine2 = type_human2 = str2
type_machine3 = type_human3 = str3
type_human = eval('type_human' + str(type_human_int))
# print("type_human_int%s : %s" % (type_human_int,type_human))
print("人出的是：%s" % type_human)
# 通过eval函数反查人通过数字出的手型

type_machine = eval('type_machine' + str(type_machine_int))
# print("type_machine_int%s : %s" % (type_machine_int,type_machine))
print("电脑出的是：%s" % type_machine)
# 通过eval函数反查输出电脑出的手型


if type_human_int == type_machine_int:
    print("你和电脑手型一样，平局！")
elif int(type_human_int) - int(type_machine_int) == 1:
    print("很遗憾，电脑赢了！")
elif int(type_human_int) - int(type_machine_int) == -2:
    print("很遗憾，电脑赢了！")
else:   
    print("恭喜，你赢了！")
# 对转换后的手型对应数值进行比较判断


