# poly.py


class Shape:
    def draw(self):
        pass

class Point(Shape):
    def draw(self):
        print("正在画一个点")

class Circle(Point):
    def draw(self):
        print("正在画一个圆")

def my_draw(s):
    s.draw()    # 调用？？方法呢？在运动时动态决定调用的方法
                # s.draw调用谁是在运行时由s的类型动态决定

s1 = Circle()
s2 = Point()
my_draw(s1)
my_draw(s2)

