# author: wp
# 2022年03月28日 23:12
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
# from rest_framework.viewsets import ModelViewSet

# 用作view 类视图
urlpatterns = [
    path('', views.api_root),  # 为api_root视图添加路由
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),  # as_view方法会判断请求的方法，从而调用相应的方法
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    # 为高亮代码片段添加一个url模式
    path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]
# 为了让url支持json
urlpatterns = format_suffix_patterns(urlpatterns)
