# coding: utf-8

s1 = '_1234.exe'

in_1 = input(">>:")

a = in_1.split(s1)

out_1 = [len(a) - 1, ]
x = 0
for i in a[:-1]:
    for j in i:
        x += 1
    out_1.append(x)
    x += len(s1)
for i in out_1:
    print(i, end=' ')
