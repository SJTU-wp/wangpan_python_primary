# author: wp
# 2022年03月28日 23:12
from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter


# 注释这部分是视图集
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# # 用作view 类视图
# urlpatterns = [
#     path('', views.api_root),  # 为api_root视图添加路由
#     path('snippets/', views.SnippetList.as_view(), name='snippet-list'),  # as_view方法会判断请求的方法，从而调用相应的方法
#     path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
#     # 为高亮代码片段添加一个url模式
#     path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view(), name='snippet-highlight'),
#     path('users/', views.UserList.as_view(), name='user-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
# ]
# # 为了让url支持json
# urlpatterns = format_suffix_patterns(urlpatterns)

# 使用了路由器
from snippets.views import SnippetViewSet, UserViewSet

router = DefaultRouter()  # 帮我们做了list, detail的方法跳转对应
router.register(r'snippets', SnippetViewSet, basename="snippet")
router.register(r'users', UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('api/', include((router.urls, 't1'), )),  # t1就是app的名字
]
