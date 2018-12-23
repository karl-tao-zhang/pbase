# # my_integer.py
# def my_integer(n):
#     i = 1    #　先初始化变量i将其设置为初始值
#     while i < n:    #循环判断是否已到终止点，如果未到则生成
#         yield i     #生成整数
#         i += 1      #控制循环条件

# for x in my_integer(10000):
#     print(x)    #1  2  3  4

# 练习：
# 　　写入函数，myodd(start,stop)用于生成start开始到stop结束,
# (不包含stop)的所有奇数



def myodd(start, stop):
    i = start
    while i < stop:
        if i % 2 :    #等同于if i % 2 == 1:
            yield i
        i += 1



L = [x for x in myodd(1,10)]
print(L)    #[1,3,5,7,9]
for x in myodd(10,20):
    print(x, end=" ")    #11, 13, 15, 17, 19
print()



