# 1976.py
# 练习：
# 　　1.写一个程序，读入任意行的文字信息，当输入空行时结束输入
# 　　将读入的字符串存于列表中，然后将列表里的内容写入的文件
# 　　input.txt　中
#   2.写一个程序,从input.txt　中读取之前输入的数据,存入列表中,再加上行号进行打印显示
#   　　显示格式如下：
#        第１行：　zzzzz
#        第２行：　xxxxx


def fn():
    L = []
    while True:
        n = input("请输入:")
        if not n:
            break
        L.append(n)
    return L


def fx(L):
    try:
        #打开文件
        f = open('input.txt', 'w')
        #写入数据
        for line in L:
            f.write(line)
            f.write('\n')    #写入换行符('\n','\r\n')

        #关闭文件
        f.close()
    except IOError:
        print("打开文件失败")


def main():
    lst = fn()
    print(lst)
    # try:
    fx(lst)

main()





































# def fn():
#     L = []
#     while True:
#         n = input("请输入:")
#         if not n:
#             break
#         L.append(n)
#     return L

# def fx(L):
#     try:
#         f = open("input.txt",'w')  #　以只写的方法打开文件

#         for i in fn():
#             f.write(i)


#         f.close()
#     except IOError:
#         print("打开文件失败")

