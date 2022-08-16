# Replacing elements of list
ls = [12, 12, 13, 12, 22, 33]
for index, item in enumerate(ls):
  ls[index] = 0
print(ls)