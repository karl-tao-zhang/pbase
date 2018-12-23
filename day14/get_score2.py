# 练习：
# 写一个函数　get_score()　来获取用户输入的学生成绩(0~100的整数)，
# 如果输入出现错误，则此函数返回0，
# 如果用户输入的数是0~100之间的数，返回这个数

def get_score():
    i = input("0~100:")
    try:
        s = int(i)
    except ValueError:
        return s
    if 0 <= s <= 100:
        return s
    return 0

score = get_score()
print('学生的成绩是：',score)


