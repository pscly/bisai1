# for n in range(400,500):
#     i = n // 100
#     j = n // 10 % 10
#     k = n % 10
#     if n == i ** 3 + j ** 3 + k ** 3:
#         print(n)


# 第一道题(16)
# input("请输入(第一次):")
# s1 = input("请输入(第二次):")

# l1 = s1.split(' ')
# l2 = []
# for i in l1:
#     if i.isdigit():
#         l2.append(int(i))

# for i in l2:
#     if not (i % 6):
#         print(i, end=" ")

# 第二道题(17)
out_l1 = []
def jisuan(str_num):
    he1 = 0
    global out_l1
    if len(str_num)>2:
        return None
    for i in l1():
        he1 += int(i)**2

    if he1 > int(str_num):
        out_l1.append(str_num)
    return None

while 1:
    in_1 = input("请输入数值:")
    nums = in_1.split(' ')











