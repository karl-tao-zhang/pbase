# human_mansge.py



class Human:    # 人类
    total_count = 0
    def __init__(self, n, a, add='未填写'):
        self.name = n
        self.age = a
        self.address = add
        self.__class__.total_count += 1

    def __del__(self):
        self.__class__.total_count -= 1

    @classmethod
    def get_human_count(cls):
        return cls.total_count    # 返回总人数

    def show_info(self):    # 用来显示人的信息
        print(self.name, '今年', self.age, 
              '岁, 家庭住址:', self.address)
    def update_age(self):    #方法用来让这个人的年龄增加
        self.age += 1

def input_human():
    # 输入
    L = []
    while True:
        n = input('请输入姓名')
        if not n:
            break
        a = int(input("请输入年龄"))
        add = input("住址:")
        L.append(Human(n, a, add))
    return L


def main():
    docs = input_human()
    print("当前的总人数是", Human.get_human_count)
    docs += input_human()
    print("当前的总人数是", Human.get_human_count)

main()    #调用主函数运行