def f1():
    print("开始盖房子打地基．．．")
    return -1      # -1 代表挖出文物
    print("地基完工")
    return 0

def f2():
    print("开始盖房子地面以上的部分")
    return -2      #　代表要建高压线
    print("房子完工")

def f3():
    """第二承包商找人干活"""
    r = f1()
    if r < 0:
        return r
    else:
        r2 = f2()
        return r2


def build_house():
    r = f3()
    if r < 0:
        return r
    return 0



r = buld house()
if r == 0:
    print("房子盖好了")
else:
    print("房子没盖成，因为文物问题")
elif r == -2:
    print("房子没盖成，因为高压线问题")


# def f1():
#     print("开始盖房子打地基．．．")
#     print("地基完工")


# def f2():
#     print("开始盖房子地面以上的部分")
#     print("房子完工")

# def f3():
#     """第二承包商找人干活"""
#     f1()
#     f2()

# def build_house():
#     f3()

# buld house()
# print("房子盖好了")


