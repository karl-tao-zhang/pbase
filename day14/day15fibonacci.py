# # day15.py
# 练习：
# 　　1.用生成器函数生成斐波那契数列的前n个数：
#   　　　　１　１　２　３　５　８　１３　　．．．
#
#       def fibonacci(n):
#           ...
#           yield ..
#       1)输出前　２０　个数

def fibonacci(n):
    count = 0    #　记录当前已生成的数的个数
    if count >= n:    #判断当前已生成的个数大于等于徐娅偶的个数时，直接返回
        return
    yield 1    #　生成１
    count += 1    # 已生成的个数加１

    if count >= n:    #　再次判断已生成数的个数
        return
    yield 1    # 生成一个１
    count += 1    #　已生成个数加１

    # 用列表生成第三个起的数
    a = 1    # a代表倒数第二个数
    b = 1    # b代表倒数第一个数
    #　如果已生成的个数小于需要的个数，则继续生成
    while count < n:
        #　从第三个起
        a, b = b, a + b    #a+b是需要生成的数
        yield b    #返回刚生成的数
        count += 1    #已生成的个数加１



    # yield 3  
    # yield 5

# 1) 输出前　20 个数
for x in fibonacci(20):
    print(x)





#       ２）求前　３０　个数的和
print(sum(fibonacci(30)))





#   2.写程序打印杨辉三角(只打印６层)
#
#                 1
#                1 1
#               1 2 1
#              1 3 3 1
#             1 4 6 4 1
#            1 5 10 10 5 1
#
