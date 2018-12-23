# student_info.py


class Student:
    def __init__(self, n, a, s):
        self.name = n
        self.age = a
        self.score = s
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
        stu = Student(n, a, s)



        L.append(stu)  # 　将学生对象加入到列表
    return L    # 返回生成的列表给调用者


def ouput_student(lst):
    # 打印学生信息
    # print(lst)
    for stu in lst:
        print("姓名：", stu.name,
              "年龄：", stu.age,
              "成绩：", stu.score)


def main():
    L = input_student()
    ouput_student(L)


main()

