tuple = ('周杰伦',11,['football','music'])
check = tuple.index(11)
print(f"{check}")
print(f"{tuple[0]}")
del tuple[2][0]
print(f"{tuple}")
tuple[2].append('coding')
print(f"{tuple}")
