# 介绍

全国高校计算机能力挑战赛

> 代码提交说明：
> 1.请严格按照每道题目给出的输入/输出样例编写相关I/O代码，数字间的默认间隔是一个空格，浮点数的默认输出精度是保持小数点后2位。样例以外的提示信息请不要在屏幕上输出。
> 2.请大家确保提交的代码可以在指定的编译条件下正确地编译执行，否则自动评测程序将给出编译错误或运行时错误的信息。
> 3.每道编程题目，如果没有特殊说明，需要在1秒内完成程序的运行和输出结果，超过这个时间限制将会被判超时，失去相应测试用例的分数。每个可执行文件可使用的空间不得大于1MB。
> 4.每道编程题会有多个测试用例，每通过一些测试用例可以获得相应的分值，但只有通过全部测试用例才能拿到这题全部的分数。







## 16

16.给定两个整数N和M(0<N<M<100000)，求N到M中满足如下条件的数字，该数字与相邻的前、后数字之和可以被4整除。比如N=3，M=9时，4、8 是满足条件的， 而5、6、7不满足，3和9因为前、后数字不在N到M中，不参与统计。
输入说明：两个正整数N和M（N<M<100000）
输出说明：满足要求的数字，如果有多个满足条件的数字，按出现次序输出前3个，如果不足3个，用-1补充。
输入样例1：11 100
输出样例1：12 16 20

输入样例2：3 9
输出样例2：4 8 -1

```python
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
```





## 17

> 17.输入一个包含N个整数的数组，从中找到连续M个数之和最大的数字组合。
> 输入说明：第一行是两个正整数N（N<200）和M(M<20)
> 第二行是N个整数（每个数字Ni都是整数，且|Ni|<100000），中间用空格分开
> 输出说明：最大的M个连续数字和及第一个数在数组中的位置（初始位置按1进行计算）。
> 输入样例：10 4
> 1 2 3 4 5 6 7 8 9 10
> 输出样例：34 7

```python
'''
10 4
1 2 3 4 5 6 7 8 9 10

< 34 7
'''
# M个数字的和 怎么加最大
```

```python
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

```



## 18

> 18.计算网络数据包中的可能被注入病毒片段信息，经过长期观察发现，计算机病毒文件源码中往往包含“_1234.exe”的字符片段。现在请你开发一个计算程序，辅助信息专家检测这个病毒嫌疑特征。
> 输入说明：一个字符串S
>
> 输出说明：字符串中包含”_1234.exe”字符片段的位置，如果包含多个病毒嫌疑特征片段，输出数量后，再输出每个片段的位置。如果没有检测到病毒嫌疑片段，就输出0
>
> 输入样例：ox123_0212_3323_1234.exe20202020202_1234.exe
>
> 输出样例：2 15 35

```python
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
```



## 19

> 19.游戏中的地图都是用二维数组表达的，每个位置表示一个整数表示高度，现在需要找出地图中的最高山峰放置宝物。已知表示地图中各点的高度，用二维数组存放，请找出其中最高的山峰。二维地图中山峰的定义是该点上、下、左、右四个方向的高度值都小于该点的高度值（边界上的点不满足山峰的定义）。
> 输入说明：第一行是整数N(0<N<1001)，表示二维数组的行数和列数。
> 接下来是一个N行、N列的二维整数矩阵，每个数字表示地图上该点处的地面高度Hij(0<Hij<2020)。
> 输出说明：用于藏宝的最高山峰位置的坐标i、j（1<=i,j<=N），其中i表示行，j表示列。如果不存在满足条件的山峰，输出-1 -1。测试数据不存在多个同样高度的最高山峰。
> 输入样例：6
> 0 3 0 0 1 1
> 0 6 0 1 1 1
> 9 9 9 7 5 3
> 6 5 3 5 3 3
> 5 6 6 6 7 6
> 3 4 4 5 5 5
>
> 输出样例：5 5