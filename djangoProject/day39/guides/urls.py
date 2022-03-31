# author: wp
# 2022年03月31日 23:24
from django.urls import path
# from django.urls import re_path
from guides.views import FileUploadView, simple_html_view

urlpatterns = [
    # re_path(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view()),
    path('upload/<str:filename>/', FileUploadView.as_view()),
    path('simple_html_view/', simple_html_view),
]
