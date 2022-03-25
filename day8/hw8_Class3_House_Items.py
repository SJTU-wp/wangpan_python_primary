# 练习房子-家具类设计，感受类的设计的先后顺序

# 创建家具类
class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name, self.area)


# 创建房子类
class House:
    def __init__(self, house_type, area):
        self.type = house_type
        self.area = area

        # 剩余面积
        self.free_area = area

        # 家具名称列表
        self.item_list = []

    def __str__(self):

        return ("户型：%s\n总面积：%.2f[剩余：%.2f]\n家具：%s"
                % (self.type, self.area, self.free_area, self.item_list))

    # 类方法
    def add_item(self, item):
        print("要添加 %s" % item)
        if item.area > self.free_area:
            print("%s 的面积太大，不能添加到房子中" % item.name)
        else:
            self.item_list.append(item.name)
            self.free_area -= item.area

            return


if __name__ == '__main__':
    # 创建家具
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)

    print(bed)
    print(chest)
    print(table)

    # 创建房子对象
    my_home = House("三室两厅", 130)

    my_home.add_item(bed)
    my_home.add_item(chest)
    my_home.add_item(table)

    print(my_home)
