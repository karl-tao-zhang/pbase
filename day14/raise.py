# raise.py


#此示例示意raise语句的用法
def make_except(n):
    #假设n必须是0~100之间的数
    print("begin ...")
    if n > 100:  #传过来的参数无效，怎么告诉调用者呢?
        pass
    print("end ...")


make_except(1000)












