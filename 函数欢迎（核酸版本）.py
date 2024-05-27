def hi_hesuan():
    print("欢迎！")
    print("请出示您的健康码以及72小时核酸证明！")

    
hi_hesuan()


temperature = float(input("请输入您的体温"))
def t_hesuan(x):
    if x <= 37.5:
        print(f"欢迎！\n请出示您的健康码以及72小时核酸证明，并配合测量体温！\n您的体温是{temperature}°，体温正常请进！")
    else:
        print(f"欢迎！\n请出示您的健康码以及72小时核酸证明，并配合测量体温！\n您的体温是{temperature}°，需要隔离！")

t_hesuan(temperature)
