import random
answerint = random.randint(1,4)
print("i love python")
i = int(0)
answer1 = '我什么都喜欢'
answer2 = '我喜欢小鹿'
answer3 = '我喜欢魅惑魔女'
answer4 = '我也不知道'
answer = str()
if answerint == 1:
    answer = answer1
elif answerint == 2:
    answer = answer2
elif answerint == 3:
    answer = answer3
elif answerint == 4:
    answer = answer4
else:
    pass
temp = input("你知道我喜欢什么吗？\n")
guess = str(temp)
while (guess != answer) and (i <= 3):
    temp = input("你再猜猜呗\n")
    guess = str(temp)
    if guess == answer:
        print("发现了敌人的踪迹！")
    else:
        print("你猜的不对哦")
        i = i + 1
if guess == answer:
    print ("太棒了，你猜对啦！！！")
elif guess != answer:
        print ("下次一定会更好！")
print("你会变得更厉害的！")