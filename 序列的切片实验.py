str = '万过薪月，员序程马黑来，onhtyP学'
cut = str[5:10]
cut_1 = cut[::-1]
print(f"{cut_1}")

split = str.split(',')
print(f"{split}")
change = split[0].replace('来','')
print(f"{change}")
reverse = change[-9:-14:-1]
print(f"{reverse}")
