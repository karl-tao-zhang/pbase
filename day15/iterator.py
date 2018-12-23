# iterator.py

# L = [2,3,5,7]
#用for循环来访问可迭代对象中的数据

# for x in L:
#     print(x)

# print('---------------------------------')
#用while循环能否访问可迭代对象中的数据？
#第一步，让L给我么一个迭代器

# it = iter(L)

#第二部，循环用it迭代器去获取L中的数据,
#     直到StopIteration为止

# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break


# 练习：
#   已知有一个集合：
#   　　s = {"工商银行", "建设银行", "中国银行", "农业银行"}
#     1.用for语句遍历集合中的元素并打印
#     2.将上面的for语句改写为while语句实现上面同样的功能
#     　　　　提示：用　iter　和　next　函数实现
s = {"工商银行", "建设银行", "中国银行", "农业银行"}
# for i in s:
#     print(i)

it = iter(s)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break

