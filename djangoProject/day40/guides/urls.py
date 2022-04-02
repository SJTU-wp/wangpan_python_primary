# author: wp
# 2022年03月31日 23:24
from django.urls import path
# from django.urls import re_path
from rest_framework.routers import DefaultRouter
from guides.views import *

router = DefaultRouter()  # 帮我们做了list，detail的方法跳转对应

router.register(r'comments', CommentViewSet)
router.register(r'events', EventViewSet)
router.register(r'event1s', Event1ViewSet)
router.register(r'albums', AlbumViewSet)
router.register(r'tracks', TrackViewSet)

urlpatterns = [
    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('upload/<str:filename>/', FileUploadView.as_view()),
    path('simple_html_view/', simple_html_view),
]

urlpatterns += router.urls
