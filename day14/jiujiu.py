# 练习：
# 　　１．一个球从100米高度落下，每次落地后反弹高度为原高度的一半，再落下，
# 　　　　１）写程序算出皮球从第10次落地后反弹高度是多少？
# 　　　　２）球共经过多少米路径？
# def fn(n):
#     L = []
#     i = 1
#     s = 100
#     while i <= n:
#         s /= 2
#         # L.append(s)
#         i += 1
#     return s

# z = fn(10)
# print(":",z)



# def fn1(m):
#     L = []
#     for i in range(1, m):
#         L.append(fn(i))
#         s = sum(L) * 2 + fn(m) + fn(0)
#     return s


# print(fn1(10))






# 　　２．打印九九乘法表：
# 　　　　　１＊１＝１
#     　１＊２＝２　２＊２＝４
# 　　　　　１＊３＝３　２＊３＝６　３＊３＝９
# 　　　　　　．．．．．．
# 　　　　　１＊９＝９．．．．．．．．９＊９＝８１
# def fn():
#     for i in range(1, 10):  #1
#         for j in range(1, i + 1):  #1
#             print(j,"*",i,"= ", i * j, end = ' ')
#         print()
# fn()


# 　　３．分解质因数：
# 　　　　　输入一个正整数，分解质因数：
#     　如输入：９０　＝　２＊３＊３＊５
#     　(质因数是指最小能被原数整除的素数(不包含１))


#1
# def func(num):
#     for i in range(2,int(num/2+1)):
#         if num % i == 0:
#             print(i,end='')
#             print('*',end='')
#             return func(num//i)
#             #用来获取质因数分解的最后一个因素
#     print(num)
# print(func(63))


#2
# num = int(input("请输入一个数:"))
#     #num1 = int(num/2+1)
# i = 2
# while i < int(num/2+1):
#     if num % i == 0:
#         print(i,end='')
#         print('*',end='')
#         num //= i
#     else:
#         i += 1
# print(num)

#3
# num = int(input("请输入一个数:"))
# i = 2
# while num != 1:
#     if num % i == 0:
#         print(i,end='')
#         print('*',end='')
#         num //= i
#     else:
#         i += 1
# print('结束',i)























