# day19.py
# 　３．写一个实现迭代器协议的类　Primes 让此类可以生成从b开始的n个不素数


class Primes:
    @staticmethod
    def __isprime(x):
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

    def __init__(self, b, n):
        self.begin = b
        self.count = n

    def __iter__(self):
        self.cur_pos = self.begin    # 设置迭代的起始值
        self.cur_coint = 0
        return self

    def __next__(self):
        # 已完成生成，不需要再生成，我停止迭代
        if self.cur_coint >= self.count:
            raise StopIteration
        self.cur_coint += 1    # 计数加１
        while True:
            if self.__isprime(self.cur_pos):
                v = self.cur_pos
                self.cur_pos += 1
                return v
            self.cur_pos += 1    # 为下一次循环做准备


for x in Primes(10, 4):
    print(x)    # 11 13 17 19
