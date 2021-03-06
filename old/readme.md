# 介绍

全国高校模拟题的编程题目部分解释



> 代码提交说明：
> 1.请严格按照每道题目给出的输入/输出样例编写相关I/O代码，数字间的默认间隔是一个空格，浮点数的默认输出精度是保持小数点后2位。样例以外的提示信息请不要在屏幕上输出。
> 2.请大家确保提交的代码可以在指定的编译条件下正确地编译执行，否则自动评测程序将给出编译错误或运行时错误的信息。
> 3.每道编程题目，如果没有特殊说明，需要在1秒内完成程序的运行和输出结果，超过这个时间限制将会被判超时，失去相应测试用例的分数。每个可执行文件可使用的空间不得大于1MB。
> 4.每道编程题会有多个测试用例，每通过一些测试用例可以获得相应的分值，但只有通过全部测试用例才能拿到这题全部的分数。



## 编程题1  (16)

> 16.将整数数组中是6的倍数的元素按照输入次序依次输出。如果没有符合条件的元素则输出-1。
> 输入说明：第一行是整数N（N<10000），表示数组中的元素个数，第二行是这个数组中的N个元素，规定元素中至少包含一个满足条件的元素。
> 输出说明：输出数组序列中6的倍数，如果有两个以上满足条件的元素，中间用空格隔开。
> 输入样例：6
> 2 3 6 12 28 45
> 输出样例：6 12





## 编程题2 (17)

> 17.对于整数区间[N，M]，已知0输入说明：两个整数N 和M。
> 输出说明：顺序输出元素数位上各个数字的平方和大于元素本身的数。
> 输入样例：21 25
> 输出样例：25
> 说明：例如22的数位数字为2,2，这两个数字的平方和为8，小于22，不满足筛选条件所以不输出；25的数位数字为2,5，这两个数字平方和为29，大于25，满足筛选条件，所以将25输出。





## 编程题3 (18)

> 18.输入一串字符，由字母、数字和空格组成，长度<1000，判断其中是否存在日期格式的数据。日期格式的数据具有如下的特征，连续包含年份和月份信息。年份信息是指连续的四个数字，之后是Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec这些字符串之一,如”2019Nov”就是符合日期格式要求的数据。
> 输入说明: 输入一个字符串。
> 输出说明: 输出包含满足日期格式的字符子串；如果不包含，则输出2000Jan。
> 输入样例1: Todayis2019Nov15th.
> 输出样例1： 2019Nov
> 输入样例2: Todayisasunnyday.
> 输出样例2： 2000Jan
> 输入样例3: OnNov05，nothing happen.
> 输出样例3： 2000Jan



## 编程题4 (19)

> 19.有一个DNA序列，用字符串S表示（仅包含’A’、’C’、’G’、’T’四种字符，长度<100000）。现有N个待检测的基因片段（序号分别是1,2,…,N），用字符串Ti（i=1,2,…,N）表示（仅包含’A’、’C’、’G’、’T’四种字符，长度<1000）。请分别检测DNA序列S中是否存在这些基因片段，并按下面输出说明格式依次输出检测结果。
> 输入说明：第一行是DNA序列S。
> 第二行是正整数N，表明有N个待检测的基因片段，之后有N行，分别表示这N个待检测的基因片段，即每行一个基因片段。
> 输出说明：依次匹配这N个待检测的基因片段，如果DNA序列S中存在第i个待检测的基因片段，输出Ti: ALERT 所在位置（即Ti的首字母在S中的位置，如果出现多次，输出第一次出现的位置，S的起始位置为1）；如果不存在则输出Ti: SAFE。
> 输入样例：ATCGCGCGAATTGATCGTTCGA
> 2
> AATTGAT
> GATCGTC
> 输出样例：T1: ALERT 9
> T2: SAFE



## 编程题5 (20)

> 20.某机械公司生产两种产品。A的单件利润分别是100元，B的单件利润是150元。每种产品由三种材料构成，现给出每种材料的库存（库存小于100000），求利润最大的生产方案。
> 输入说明: 第一行给出生产每件A产品所需要的三种材料数量；
> 第二行给出生产每件B产品所需要的三种材料数量；
> 第三行给出三种材料的库存数量。
> 输出说明: 输出利润最大生产方案所对应的每种产品的生产数量（按照产品A、产品B的顺序）和利润最大值，每个数值间用空格隔开。
> 输入样例: 3 1 2
> 5 2 2
> 30 4 6
> 输出样例：2 1 350
>
> 样例信息提示：每件产品A需要材料一3、材料二1、材料三2；每件产品B需要材料一5、材料二2、材料三2。目前库存材料一为30、材料二为4、材料三为6。采用生产A产品2件、B产品1件的生产方案，利润为350，达到利润最大值。


