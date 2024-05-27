str = 'itheima itcast boxuegu'
num = str.count('it')
print(f"字符串中有：{num}个it字符")
replace = str.replace(' ','|')
print(f"字符串被替换空格后，结果：{replace}")
split = replace.split('|')
print(f"字符串按照|分割后，得到：{split}")
