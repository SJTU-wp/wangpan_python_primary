# 实现单例模式
# 借助类属性，外加重写__new__方法
class MusicPlayer(object):
    instance = None  # 借助类属性，充当判断条件

    @classmethod  # 不写这个的话，对象/实例也能充当cls的角色
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            # 创建对象时，new方法会被自动调用
            print("创建对象，分配空间")

            # 为对象分配空间
            cls.instance = super().__new__(cls)

        # 返回对象的引用
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
