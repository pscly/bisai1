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
def bian_int_list(l1):
    re_l1 = []  # 返回出去的列表
    for i in l1:
        re_l1.append(int(i))
    return re_l1

def jisuan(int_num):
    he1 = 0
    global out_l1

    for i in str(int_num):
        he1 += int(i)**2

    if he1 > int(str_num):
        out_l1.append(str_num)
        return True
    return None

while 1:
    in_1 = input("请输入数值:")
    nums_l1 = in_1.split(' ')
    
    for i in range(nums_l1[0, nums_l1[1]+1]):
        if jisuan(i):
            
        











