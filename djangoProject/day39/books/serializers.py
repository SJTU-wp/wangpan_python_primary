# author: wp
# 2022年03月28日 20:45
from rest_framework import serializers
from books.models import BookInfo


class BookInfoSerializer(serializers.ModelSerializer):
    """专门用于对图书进行序列化和反序列化的类: 序列化器类"""
    class Meta:
        # 当前序列化器在序列化数据的时候,使用哪个模型
        model = BookInfo
        # fields = ["id","btitle"] # 多个字段可以使用列表声明,如果是所有字段都要转换,则使用 '__all__'
        fields = '__all__'  # 多个字段可以使用列表声明,如果是所有字段都要转换,则使用 '__all__'
