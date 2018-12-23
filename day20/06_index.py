# 02_mylist.py

# 此示例索引 index 和切片　slise 运算符的重载

# class MyList:
#     def __init__(self, iterable):
#         self.data = [x for x in iterable]

#     def __repr__(self):
#         return 'MyList(%r)' % self.data

    
#     def __contains__(self, e):    # e代表测试元素
#         print("__contains__被调用")
#     for x in self.data:
#         if e == x:    # 如果相同，则说明e就在列表中
#         return True
#     return False


# L1 = MyList([1,-2, 3, -4, 5])
# if 2 in L1:    # 需要重载　__contains__方法
#     print("２在L1中")
# else:
#     print("２不在L1中")


class MyList:
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%r)' % self.data

    
    def __getitem__(self, i):
        print("__getitem__被调用", i)
        return self.data[i]

    def __setitem__(self, i, v):
        self.data[i] = v


L1 = MyList([1,-2, 3, -4, 5])
print(L1[2])
L1[1] =  2
print(L1)