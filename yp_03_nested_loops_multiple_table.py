# 循环嵌套联系
def function_print():
    i = 0
    while i <= 5:
        print("*" * i)
        i += 1
    print("第一句", end="")
    print("第二句", end="")
    print("")
    # print函数增加参数语句（end="xxx"）可将自动换行替换为需要的语句


def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print("%d * %d = %d"% (col, row, col * row), end="\t")
            # 用转义字符\t(横向制表符)对齐表达式

            # print("%d * %d = %d" % (col, row, col * row), end="")
            # if col * row < 10:
            #     print("   ", end="")
            # else:
            #     print("  ", end="")
            # # 用输出空格来对齐表达式

            col += 1

        print("")
        # 输出换行符

        row += 1


# print("间隔测试")

# multiple_table()
# 输入函数名直接并执行调用函数