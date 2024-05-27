#\n 换行符

# print输出不换行
print("hello")
print("world")

print("hello", end='') #end=''即可取消此行空格
print("world\n")

#\t 使多行字符对齐 （效果等同于在键盘上按下TAB键）
#制表符号
print("hello world")
print("itheima best")

print("hello\tworld")
print("itheima\tybest\n")

print("w\t\t*")
print("ww\t\t*")
print("www\t\t*")
print("wwww\t*")
print("wwwww\t*")
print("wwwwww\t*")
print("wwwwwww\t*")
print("wwwwwwww*\n")

"""
not ture == false
not false == ture
"""

#在函数内修改全局变量
"""global
函数内部global在里面修改外面也改变
"""
num =20
def text1():
    global num
    print(f"{num}")
    num -= 10
    print(f"{num}")

text1()
print(f"{num}")

#############数据容器##################################
#index查找指定元素在列表的下标，如果找不到，报错ValueError
list = [1,2,3]
index = list.index(2)
print(f"{index}")

#重新赋值
list[1] = 0
print(f"{list}")

#插入元素 insert
list.insert(1,'牛')
print(f"{list}")
list.insert(-1,'牛的')
print(f"{list}")

#追加元素 append extend
#将指定元素追加到列表的尾部
#append 追加一个元素 extend 将另一个列表的所有元素追加
list.append(True)
print(f"{list}")
List = [3,2,1]
list.extend(List)
print(f"{list}")

#删除元素
#del pop
del list[3]
print(f"{list}")
gain = list.pop(3)
print(f"{list}\n{gain}")

#删除某元素在列表中的第一个匹配项 remove
#删除元素而不是位置
list.remove(1)
print(f"{list}")
list.remove(True)
print(f"{list}")

#清空整个列表 clear
list.clear()
print(f"{list}")

#统计某元素在列表内数量 count
my_list = [1,1,2,2,2,3]
count = my_list.count(2)
print(f"{count}")

#统计列表里共有多少元素 len
number =  len(my_list)
print(f"{number}")

##########元组#########################################
#两种形式
#元组为无法更改的列表
#************一个元素的元组结尾需要加，***************
yuanzu = ()
yuanzu = tuple()

#########字符串#########################################
#字符串的替换 replace
string = 'hello hi'
str = string.replace('hello','hi')
print(f"{string}")
print(f"{str}")

#字符串的分割
#将字符串划分为多个字符串，并存入列表对象中 split
string_1 = 'hello python hi'
list_1 = string_1.split(' ')
print(f"{list_1}")

#字符串的规整操作
#字符串的规整操作（去前后(首尾）空格） 字符串.strip( )
#（去前后(首尾）指定字符串） 字符串.strip(字符串)
#若首尾有空格等任意字符则第二种去掉字符串的无法实现
str_1 = '             102hi hello python021        '
str_strip_1 = str_1.strip( )
print(f"{str_strip_1}")
str_1 = '102hi hello python021'
str_strip_2 = str_1.strip('12')
print(f"{str_strip_2}")
str_1 = '12hi hello python021'
str_strip_3 = str_1.strip('12')
print(f"{str_strip_3}")

########序列切片########################################
#切片：从一个序列中取出一个子序列
#序列[起始下标：结束下标：步长]
#起始下标留空表示从头开始 结束下标留空表示取到结尾
str_2 = [0,1,2,3,4,5,6]
cut = str_2[2:5:1]
print(f"{str_2}")
print(f"{cut}")

###########集合  set  #####################################
set1 = {1,2,3}
set2 = {1,5,6}
#集合内添加元素 add
set1.add(0)
print(f"{set1}")
#取两个集合的差集 集合1.difference(集合2)
#新集合不影响旧集合
set3 = set1.difference(set2)
set4 = set2.difference(set1)
#注意set3与set4的区别
print(f"{set3}")
print(f"{set4}")

#消除两个集合的差集 集合会变化
#集合1.difference_update(集合2) 集合1 2 可换位 结果不一样
set1 = {1,2,3}
set2 = {1,2,6}
set1.difference_update(set2)
print(f"{set1}")
set1 = {1,2,3}
set2.difference_update(set1)
print(f"{set2}")
#两个集合合并为一个
#集合1.union(集合2)
set5 = set1.union(set2)
print(f"{set5}")
set6 = set2.union(set1)
print(f"{set6}")

######################字典######################
# dict = {key:value,key:value}
dict = {'一':1,'二':2,'三':3}
num = dict['二']
print(f"{num}")

#新增（更新）元素
dict['四'] = 4
print(f"{dict}")

#删除元素 pop
num_1 = dict.pop('一')
print(f"{dict}")
print(f"{num_1}")

#清空元素 clear

#获取全部的key
#keys()
keys = dict.keys()
print(f"{keys}")

#遍历字典
#方法一
for x in keys:
    print(f"{x}",end='')
    print(f"{dict[x]}")

for x in dict:
    print(f"{x}",end='')
    print(f"{dict[x]}")

#统计字典内的元素数量 len


#切片
list = [1,2,3,4,5,6,7,8,9]
list[2:5] = [3,4,5,6]
list[5] = [1,2,3,4,5,6]
list[0] = [1]
