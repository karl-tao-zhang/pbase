# # day15.py
# 练习：
# 　　1.用生成器函数生成斐波那契数列的前n个数：
#   　　　　１　１　２　３　５　８　１３　　．．．
#
#       def fibonacci(n):
#           ...
#           yield ..
#       1)输出前　２０　个数

# def fibonacci(n):
#     count = 0    #　记录当前已生成的数的个数
#     if count >= n:    #判断当前已生成的个数大于等于徐娅偶的个数时，直接返回
#         return
#     yield 1    #　生成１
#     count += 1    # 已生成的个数加１

#     if count >= n:    #　再次判断已生成数的个数
#         return
#     yield 1    # 生成一个１
#     count += 1    #　已生成个数加１

#     # 用列表生成第三个起的数
#     L = [1, 1]
#     #　如果已生成的个数小于需要的个数，则继续生成
#     while count < n:
#         #　从第三个起
#         L.append(L[-1] + L[-2])    #生成下一个数
#         yield L[-1]    #返回刚才生成的数
#         count += 1    #已生成的个数加１



#     # yield 3  
#     # yield 5

# # 1) 输出前　20 个数
# for x in fibonacci(20):
#     print(x)





#       ２）求前　３０　个数的和






#   2.写程序打印杨辉三角(只打印６层)
#
#                 1
#                1 1
#               1 2 1
#              1 3 3 1
#             1 4 6 4 1
#            1 5 10 10 5 1

def get_next_line(lst):

    # 第１步，先放入一个１
    next_line = [1]    #先把最左的数放进去
    # 第２步，计算中间的依赖上一层的那些数
    for i in range(len(lst) - 1):
        next_line.append(lst[i] + lst[i + 1])

    # 第３步，在最后放入一个１
    next_line.append(1)
    return next_line


def get_yanghui_list(n):
    L = [1]
    yhlist = []    # 创建一个空的列表
    for _ in range(n):
        yhlist.append(L)    #　把当前L存储的一行放入列表
        L = get_next_line(L) # 用当前行来计算处下一行
    return yhlist


L = get_yanghui_list(6) 
for x in L:
    print(x)



# L = [1]
# L2 = get_next_line(L)    #[1, 1]
# print(L2)
# L3 = get_next_line(L2)   #[1, 2, 1]
# print(L3)
# L4 = get_next_line(L3)   #[1, 3, 3, 1]
# print(L4)









