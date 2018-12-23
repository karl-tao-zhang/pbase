# student_info.py


class Student:
    pass


def input_student():
    pass
    #...获取学生信息，形成列表返回
    L = []
    while True:
        n = input("请输入姓名")    #姓名为空则结束输入
        if not n:
            break
        a = int(input("请输入年龄："))
        s = int(input("请输入成绩："))
        stu = Student()   # 创建一个学生对象
        stu.name = n    # 添加属性
        stu.age = a
        stu.score = s
        L.append(stu)  # 　将学生对象加入到列表
    return L    # 返回生成的列表给调用者


def ouput_student(lst):
    # 打印学生信息
    print(lst)
    for stu in lst:
        print("姓名：", stu.name,
              "年龄：", stu.age,
              "成绩：", stu.score)


def main():
    L = input_student()
    ouput_student(L)


main()


