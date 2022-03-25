# author: wp
# 2022年03月21日 20:15
# python通过重写来实现多态
# 多态：不同的子类对象调用相同的父类方法，产生不同的执行结果

class MiniOS(object):
    """MiniOS 操作系统类"""
    def __init__(self, name):
        self.name = name
        self.apps = []  # 安装的应用程序名称列表

    def __str__(self):
        return "%s 安装的软件列表为 %s" % (self.name, str(self.apps))

    def install_app(self, app):
        if app.name in self.apps:
            print("已经安装了 %s，无需再次安装" % app.name)
        else:
            app.install()
            self.apps.append(app.name)


class App(object):
    def __init__(self, name, version, desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return "%s 的当前版本是 %s - %s" % (self.name, self.version, self.desc)

    def install(self):
        print("将 %s [%s] 的执行程序复制到程序目录..." % (self.name, self.version))


class PyCharm(App):
    """继承App类"""
    pass


class Chrome(App):
    def install(self):
        """重写，以实现多态"""
        print("正在解压缩安装程序...")
        super().install()  # 调用父类的install方法


if __name__ == '__main__':
    linux = MiniOS("Linux")
    print(linux)  # Linux 安装的软件列表为 []

    # PyCharm继承了App类，在实例化时，应给出属性：name, version, desc
    pycharm = PyCharm("PyCharm", "1.0", "python 开发的 IDE 环境")
    chrome = Chrome("Chrome", "2.0", "谷歌浏览器")

    # 体会多态
    linux.install_app(pycharm)
    linux.install_app(chrome)

    print(linux)

    linux.install_app(chrome)
