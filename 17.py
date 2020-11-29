# coding: utf-8

def bian_int_list(l1):
    return_l1 = []
    for i in l1:
        return_l1.append(int(i))
    return return_l1


def jisuan(int_num):
    he1 = 0
    global out_l1

    for i in str(int_num):
        he1 += int(i) ** 2

    if he1 > int_num:
        out_l1.append(int_num)
        return True
    return None


in_1 = input(">>:")
m, n = bian_int_list(in_1.split(' '))
in_2 = input(">>:")
l1 = bian_int_list(in_2.split(' '))

max_num_list = []
max_num_x = 0  # 最大数的数组位置
nax_num = 0
now_num_l1 = []

for i in range(n):
    max_num_list.append(0)
    now_num_l1.append(0)

for i, j in enumerate(l1, 1):
    now_num_l1.pop(0)
    now_num_l1.append(j)
    if sum(now_num_l1) > nax_num:
        max_num_x = i  # 更新数组所在位置
        max_num_list = now_num_l1
        nax_num = sum(max_num_list)

out_1 = [sum(max_num_list), max_num_x+1-n]
for i in out_1:
    print(i, end=' ')



