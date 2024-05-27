list = [1,2,3,4,5,6,7,8,9,10]
List = []
LIST = []
index = 0
while index <= 9:
    if list[index]%2 == 0:
        List.append(list[index])
    index += 1
print(f"{List}")

for x in list:
    if x%2 == 0:
        LIST.append(x)
print(f"{LIST}")
 