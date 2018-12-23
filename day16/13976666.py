
# try:
#     f = open("data.txt")
#     print('打开文件成功')


#     n = f.read(2)
#     s = f.read(13)
#     print("姓名:", n,"电话:", s)
#     print("姓名:", n,"电话:", s)
#     print("姓名:", n,"电话:", s)


#     f.close()
#     print("文件已关闭")
# except IOError:
#     print("文件打开失败")


def data():
    f = open('data.txt')
    L = []
    while True:
        s = f.readline()
        if not s:
            f.close()  #关闭文件
            return L
        # s = '小张 13888888888\n＇
        # 去掉s右侧末尾的换行符
        s = s.rstrip()
        index = s.find(' ')
        name = s[:index]    #用切片获取到名字
        number = s[index + 1:]
        L.append((name, number))
        # print("姓名:", name, "手机号:",number)


# lst = data()
# print(lst)

def ppk(L):
    for name, number in L:
        print("姓名:", name, "手机号:",number)

ppk(data())










