# author: wp
# 2022年03月26日 21:01
# ORM实例编写练习，理解ORM要做的事情（对象，关系，映射）

class ModelMetaclass(type):
    def __new__(mcs, name, bases, attrs):
        mappings = dict()
        # 判断是否需要保存
        for k, v in attrs.items():
            # 判断是否是指定的StringField或者IntegerField的实例对象
            if isinstance(v, tuple):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        # 删除这些已经在字典中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings  # 保存属性和列的映射关系
        attrs['__table__'] = name  # 假设表名和类名一致

        return super().__new__(mcs, name, bases, attrs)


class Model(object, metaclass=ModelMetaclass):  # metaclass起两次作用
    def __init__(self, **kwargs):
        for name, value in kwargs.items():
            setattr(self, name, value)  # 对象属性设置

    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():  # 没有那么智能，联想不出来
            fields.append(v[0])
            args.append(getattr(self, k, None))

        args_temp = list()
        for temp in args:
            # 判断输入如果是数字类型
            if isinstance(temp, int):
                args_temp.append(str(temp))
            elif isinstance(temp, str):
                args_temp.append("""'%s'""" % temp)

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(args_temp))
        print('SQL: %s' % sql)


class User(Model):
    uid = ('uid', "int unsigned")
    name = ('username', "varchar(30)")
    email = ('email', "varchar(30)")
    password = ('password', "varchar(30)")


u = User(uid=12345, name='Michael', email='test@orm.org', password='my-pwd')  # 两次构造，这块最细节的地方
print(u.__dict__)
u.save()
