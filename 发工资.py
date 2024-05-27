money = 10000
for x in range(1, 21):
    if money == 0:
        print("工资发完了，下个月领取吧。")
        break
    import random
    num = random.randint(1, 10)
    if num <= 5:
        print(f"员工{x}，绩效分{num}，低于5，不发工资，下一位。")
    else:
        money -= 1000
        print(f"向员工{x}发放工资1000元，账户余额还剩{money}元。")
