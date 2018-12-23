# 05_iterator.py

# 此示例示意 bool　真值测试函数的重写
class MyList:
    """定义一个容器类，用于存储任意类型的数据
    其内部的存储方式用list实现"""
    def __init__(self, iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'MyList(%s)' % self.data

    def __iter__(self):
        '''此方法吧MyList类型的对象做为可迭代对象使用
        此方法需要返回迭代器'''
        return MyListIterator(self.data)    # retunr 迭代器



class MyListIterator:
    '''此类定义一个迭代器类，用于生成能够访问MyList对象的迭代器'''
    def __init__(self, lst_data):
        print("迭代器已创建")
        self.data = lst_data    # 绑定要访问的数据列表
        self.cur_pos = 0    # 设置迭代器的起始位置为0

    def __next__(self):
        '''此方法用来访问可迭代对象的数据，
        如果没有数据时触发异常　StopIterator
        异常来通知调用者停止迭代，即"迭代器协议" '''
        # 先判断是否索引越界
        if self.cur_pos >= len(self.data):
            raise StopIteration
        index = self.cur_pos
        self.cur_pos += 1    # 将当前位置向后移动准备下次获取
        return self.data[index]    # 返回当前位置的数据

myl = MyList([1, -2, 5, -4])

it = iter(myl)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break


# for x in (myl):
#     print(x)
