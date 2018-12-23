# day14.py

# 练习：
# 写一个函数,myfn(n),要求：
# 1.每隔１秒在屏幕打印“hello world”,共打印n次
import time
def myfn(n):
    """myfn函数是输出n遍的"hello world"
    n 为参数
"""
    s = 1
    while s <= n:
        print("hello world")
        time.sleep(1)
        s += 1
myfn(5)

# 2.请在函数中加入文档字符串：
# """myfn函数是输出n遍的"hello world"
#     n 为参数
# """


# 3.优先用递归方法完成此函数(也可以用while循环)

# 练习２：L = [1,2,2,'bob','lucy']
# 1.从L中返回随意元素
# 2.将L乱序random.shuffle(L)
# 3.从L中随意选择３个元素







