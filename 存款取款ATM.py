name = input("请输入名字")
money = 5000000
def Main_menu():
    print(f"{name}，您好，欢迎来到银行ATM。请选择操作")
    print(f"查询余额\t【输入1】\n存款\t\t【输入2】\n取款\t\t【输入3】\n退出\t\t【输入4】\n")
    choose = int(input("请输入您的选择"))
    if choose == 1:
        balance()
    if choose == 2:
        deposit()
    if choose == 3:
        Withdrawal()
    if choose == 4:
        out()
def balance():
    print(f"{name}，您好，您的余额剩余：{money}元。\n")
    Main_menu()
def Withdrawal():
    get = float(input("请问您想取多少元。"))
    global money
    money -= get
    print(f"{name}，您好，您取款{get}元成功。")
    print(f"{name}，您好，您的余额剩余：{money}元。\n")
    Main_menu()
def deposit():
    give = float(input("请问您想存多少元。"))
    global money
    money += give
    print(f"{name}，您好，您存款{give}元成功。")
    print(f"{name}，您好，您的余额剩余：{money}元。\n")
    Main_menu()
def out():
    return
Main_menu()
