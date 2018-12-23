# 　　１．一个球从100米高度落下，每次落地后反弹高度为原高度的一半，再落下，
# 　　　　１）写程序算出皮球从第10次落地后反弹高度是多少？
# 　　　　２）球共经过多少米路径？

# def ball_last_height(height,times):
#     for _ in range(times):
#         # 此处的语句会执行times次
#         height /= 2
#     return height


# def ball_distance(height, times):
#     meter = 0 # 用来累加路程的和
#     for _ in range(times):
#         meter += height    #累加下落过程的路程
#         height /= 2    # 算出反弹高度
#         meter += height    # 累加反弹过程的路程
#     return meter


# height = ball_last_height(100, 10)
# print("最后的高度是：", height)

# meter = ball_distance(100,10)
# print("球经历的路程是：", meter)


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

# for i in range(1, 10):
#     # 打印一行
#     # print(i)
#     for j in range(1, i + 1):
#         print("%dx%d=%d" % (j,i,j*i),end=' ')
#     print()



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























