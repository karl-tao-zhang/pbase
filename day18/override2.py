# override.py

# 此示例示意B类的work 覆盖A类的work

class A:
    def work(self):
        print("A类的work方法被调用")

class B(A):
    def work(self):
        print("B类的work方法被调用")

b = B()
b.work()    # B类的work方法被调用
Ａ.work(b)    #　A类的work被调用

