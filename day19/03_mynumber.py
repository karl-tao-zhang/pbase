# 03_mynumber.py


# 此示例示意　数值类型转化函数重写
class MyNumber:
    """此类是自定义的类,用于表示自定义数字的类型"""
    def __init__(self, v):
        self.data = v

    def __repr__(self):
        return 'MyNumber(%s)' % self.data

    def __int__(self):
        return int(self.data)

    def __float__(self):
        return float(self.data)
    def __bool__(self):
        return bool(self.data)

n1 = MyNumber('100')
print('n1 =', n1)
print(int(n1))    # ??
print(float(n1))  # 需要实现__float__(self)方法
print(bool(n1))