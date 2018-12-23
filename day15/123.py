# 123.py
# 练习：
# 　　写一个程序，读入任意行的文字数据，当输入空行时结束输入
# 　　打印带有行号的输入结果：
# 　　如：
# 请输入：hello<回车>
# 请输入：tarena<回车>
# 请输入：bye<回车>
# 请输入：<回车>
# 输出如下：
# 第１行：hello
# 第２行：tarena
# 第３行：bye
# def fn():
#     L = []
#     while True:
#         n = input("请输入：")
#         if not n:
#             break
#         L.append(n)
#     return L




# it = iter(enumerate(fn(), 1))
# while True:
#     try:
#         k, n = next(it)
#         print("第", k,'行:', n)
#     except StopIteration:
#         break


def input_text():
    """读入键盘输入的文本数据，形成列表后返回"""
    L = []
    while True:
        s = input("请输入：")
        if not s:
            break
        L.append(s)
    return L

def ott(L):
    for t in enumerate(L, 1):    # t = (0, "hello")
        print("第%d行: %s" % t)


def main():
    t = input_text()    # 得到用户输入的数据
    print(t)
    ott(t)
main()










