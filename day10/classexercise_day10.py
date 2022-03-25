# 1、静态方法

class Dog(object):
    @staticmethod
    def run():
        # 静态方法内不需要访问实例属性/类属性
        print("小狗要跑...")


# 通过类名.调用静态方法 - 不需要创建对象
Dog.run()


# 2、类属性-类方法实例
class Game(object):
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    # 静态方法：打印帮助
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    # 类方法，一般是类调用，？对象调用则不规范
    @classmethod
    def show_top_score(cls):
        print("历史记录 %d" % cls.top_score)

    # 对象方法
    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# （1）查看游戏的帮助信息
Game.show_help()

# （2）查看历史最高分
Game.show_top_score()

# （3） 创建游戏对象
game = Game("小明")

game.start_game()
game.show_top_score()  # ？不规范


# 3、单例模式 __new__
# 借助类属性，外加重写__new__方法
class MusicPlayer(object):
    instance = None  # 借助类属性，充当判断条件

    @classmethod  # 不写这个的话，对象/实例也能充当cls的角色
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # 1. 创建对象时，new方法会被自动调用
            print("创建对象，分配空间")

            # 2. 为对象分配空间
            cls.instance = super().__new__(cls)

        # 3. 返回对象的引用
        # print('%x' % id(instance))
        return cls.instance

    def __init__(self, music_name):
        print("播放器初始化")
        self.music_name = music_name


# 创建播放器对象
player1 = MusicPlayer('周杰伦')
print(player1.music_name)
player2 = MusicPlayer('倩女幽魂')  # 单例实现处
print(player2.music_name)
# 单例模式是为了让player1 和player2是同一个对象（内存地址相同）
print(player1)
print(player2)

# 4、捕捉异常
try:
    num = int(input('请输入一个整数：'))
    print(num)
except Exception as result:  # 出现异常才会走到except，有了except，程序不会崩溃
    print('%s 请输入整数！！！' % result)

print('you can see me')

