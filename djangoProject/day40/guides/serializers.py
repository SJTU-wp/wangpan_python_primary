# author: wp
# 2022年04月01日 21:31
from rest_framework import serializers
from guides.models import *
from rest_framework.validators import UniqueTogetherValidator


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(initial='lele@qq.com')
    # label就把原有提示换掉了，label='要含有django哦'；密码形式：style={'input_type': 'password'}
    content = serializers.CharField(max_length=200, help_text='请包含字段django')
    created = serializers.DateTimeField(allow_null=True)

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance

    # 字段级别的验证，添加validate_<field_name>方法
    def validate_content(self, value):
        """这个例子检查博客是否和django有关"""
        if 'django' not in value.lower():
            raise serializers.ValidationError('Blog post is not about Django')
        return value


# 对象级别的验证，添加.validate()方法
class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()

    def validate(self, data):
        """检查开始时间是在结束时间之前"""
        if data['start'] > data['finish']:  # data是一个字典
            raise serializers.ValidationError("finish must occur after start")
        return data


# 多个序列化类中去使用
def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')


# 联合唯一验证：UniqueTogetherValidator; 验证器validators参数
class Event1Serializer(serializers.ModelSerializer):
    GEEKS_CHOICES = (
        ("1", "One"),
        ("2", "Two"),
        ("3", "Three"),
        ("4", "Four"),
        ("5", "Five"),
    )
    name = serializers.MultipleChoiceField(choices=GEEKS_CHOICES)  # 模型类里要是字符串
    # name = serializers.CharField(min_length=3)
    # room_number = serializers.IntegerField(validators=[multiple_of_ten])
    # choices = [100, 101, 103, 105]

    # room_number = serializers.IntegerField(read_only=True)
    date = serializers.DateField(write_only=True)
    room_number = serializers.IntegerField(validators=[multiple_of_ten], error_messages={'error': '非10的倍数'})
    # date = serializers.DateField()

    class Meta:
        model = Event1
        fields = ('id', 'name', 'room_number', 'date')
        # validators必须是列表类型
        validators = [
            UniqueTogetherValidator(
                queryset=Event1.objects.all(),
                fields=('room_number', 'date')
            ),
        ]


# 序列化关系字段

class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    # StringRelatedField显示效果是 对象自身打印出来的样子，也就是str方法
    # tracks的名字必须和模型类中的related_name名字一致
    # tracks = serializers.StringRelatedField(many=True)
    # tracks = serializers.PrimaryKeyRelatedField(many=True,read_only=True) # 用的不多
    tracks = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='track-detail'
    )

    class Meta:
        model = Album
        fields = ['url', 'album_name', 'artist', 'tracks']


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
