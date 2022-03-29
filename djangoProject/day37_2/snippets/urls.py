# author: wp
# 2022年03月28日 23:12
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views
from rest_framework.viewsets import ModelViewSet

# 用作之前的view 函数视图
# urlpatterns = [
#     path('snippets/', views.snippet_list),
#     path('snippets/<int:pk>/', views.snippet_detail),
# ]
# 用作view 类视图
urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),  # as_view方法会判断请求的方法，从而调用相应的方法
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
]
# 为了让url支持json
urlpatterns = format_suffix_patterns(urlpatterns)
