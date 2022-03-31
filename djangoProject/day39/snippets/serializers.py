# author: wp
# 2022年03月28日 22:00
from rest_framework import serializers
from snippets.models import Snippet
from django.contrib.auth.models import User


# 在序列化类中没有的created字段，查询时得不到，新增也不需要提交这个字段
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    # owner.username的owner代表user对象；ReadOnlyField是无类型的，始终是只读的
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='t1:snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('id', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.HyperlinkedRelatedField(many=True, queryset=Snippet.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='t1:snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
