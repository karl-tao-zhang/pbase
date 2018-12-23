# 　　４．练习：
# 　　　　写一个Bicycle(自行车)类，有run(骑行)方法，
# 调用时显示骑行里程km
# class Bicycle:
#     def run(self, km):
#         print("自行车骑行了", km, "公里")
#     再写一个电动自行车类EBicycle继承自Bicycle,添加电池电量valume
#     属性，同时属有两个方法：

#     1.fill_charge(vol)  用来充电，vol为电量(度)
#     2.run(km)方法用于骑行，每骑行10km消耗电量1度，当电量消耗尽时
#     调用Bicycle的run方法骑行
#     并显示骑行结果
# 　　主程序:
# b = EBicycle(5)   # 创建一个电动自行车,默认电量5度
# b.run(10)         # 骑行10km
# b.run(100)         # 骑行100km
# b.fill_change(6)    # 充电6度
# b.run(70)         # 又骑行70km

class Bicycle:
    def run(self, km):
        print("自行车骑行了", km, "公里")

class EBicycle(Bicycle):
    def __init__(self, vol):
        self.valume = vol
        print("默认电量是", vol, "度")




    def fill_charge(self, vol):
        print("充电", vol, "度")

    def run

b = EBicycle(5)   # 创建一个电动自行车,默认电量5度
b.run(10)         # 骑行10km
b.run(100)         # 骑行100km
b.fill_change(6)    # 充电6度
b.run(70)         # 又骑行70km







