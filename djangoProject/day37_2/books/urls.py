# author: wp
# 2022年03月28日 20:43
from rest_framework.routers import DefaultRouter
from .views import BookInfoAPIView
urlpatterns = []

# 创建路由对象
routers = DefaultRouter()
# 通过路由对象对视图类进行路由生成
routers.register("books", BookInfoAPIView)

urlpatterns += routers.urls
