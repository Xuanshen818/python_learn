if int(input("请输入第一次猜想的数字：")) == 10:
    print("猜对啦")
elif int(input("不对，再猜一次：")) == 10:
    print("猜对啦")
elif int(input("不对，再猜最后一次：")) == 10:
    print("猜对啦")
else:
    print("Sorry，全部猜错啦，我想的是：10")
