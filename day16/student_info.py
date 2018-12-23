# 练习１：
# 写一个程序student_info.py要求运行时实现如下功能：
# $　python3 studen_info.py
# 请输入姓名：
# 请输入年龄：(将年龄转化为int类型)
# 请输入成绩：(将成绩转化为int类型)

# 要求：　　如果学生年龄和成绩输入有错误，则打印：
# "输入有误，请重新输入学生信息！"
# 然后让用户重新输入姓名、年龄、及成绩
# def fx():
#     while True:
#         try:
#             n = input("请输入姓名：")
#             a = int(input("请输年龄："))
#             s = int(input("请输入成绩"))
#         except ValueError:
#             print("输入有误，请重新输入！！！")
#             break
#     fx()
# fx()








# 练习２：
# 在练习２中的studen_info.py中添加语句，
# 实现用户在输入ctrl + c　终止程序时直接终止但不会报错

def fx():
    while True:
        try:
            n = input("请输入姓名：")
            a = int(input("请输年龄："))
            s = int(input("请输入成绩："))
        except ValueError:
            print("输入有误，请重新输入！！！")

        except KeyboardInterrupt:
            print("程序退出!")
            break

fx()

















