# author: wp
# 2022年04月01日 21:31
from rest_framework import serializers
from guides.models import *


class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField(initial='lele@qq.com')
    # label就把原有提示换掉了，label='要含有wangdao哦'
    content = serializers.CharField(max_length=200,  help_text='请发表你的心声',
                                    style={'input_type': 'password'})
    created = serializers.DateTimeField(allow_null=True)

    def validate_content(self, value):
        """
        Check that the blog post is about Django.
        """
        if 'wangdao' not in value.lower():
            raise serializers.ValidationError("content post is not about wangdao")
        return value

    def create(self, validated_data):
        return Comment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


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
