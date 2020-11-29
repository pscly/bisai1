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


out_1 = [-1, -1, -1]
in_1 = input(">>:")
nums_l1 = bian_int_list(in_1.split(' '))
out_1_x = 0
for i in range(nums_l1[0] + 1, nums_l1[1]):
    if not (i % 4):
        out_1[out_1_x] = i
        out_1_x += 1
    if out_1_x > 2:
        break

for i in out_1:
    print(i, end=' ')

