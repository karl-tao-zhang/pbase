# with.py

# 此示例示意with语句的使用方法


# # 打开文件读取文件数据(try-finally来实现关闭文件)
# def read_file():
#     try:
#         f = open("abcd.txt")
#         try:
#             while True:
#                 s = f.readline()
#                 if not s:
#                     break
#                 int(input("请输入任意数字打印下一行："))
#                 print(s)
#         finally:
#             print("文件已关闭")
#             f.close()
#     except IOError:
#         print("SOS")
#     except ValueError:
#         print("程序以转为正常状态")

# read_file()
# print("程序结束")


# 打开文件读取文件数据(try-finally来实现关闭文件)
def read_file():
    try:
        # f = open("abcd.txt")
        # with open("abcd.txt") as f:
        with open(src_file, 'rb')as fr 

            while True:
                s = f.readline()
                if not s:
                    break
                int(input("请输入任意数字打印下一行："))
                print(s)
            print("文件已关闭")

    except IOError:
        print("SOS")
    except ValueError:
        print("程序以转为正常状态")



read_file()
print("程序结束")


