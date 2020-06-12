teacher = '燕平'
print(teacher)
str = """
2
3
4
"""
print(str)

age = int(input("请输入你的年龄\n"))
if age >= 18 and age <= 55:
    print("欢迎进入")
    print("再次欢迎")
else:
    #print("你的年龄不符，不得进入！")
    if age < 18:
        print("你的年龄小于18岁，不得进入！")
    else:
        print("你的年龄超过55岁，不得进入！")
