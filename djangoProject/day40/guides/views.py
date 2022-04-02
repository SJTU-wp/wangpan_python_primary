# Create your views here.
from rest_framework import views
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import FileUploadParser
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from guides.models import *
from guides.serializers import *


class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def simple_html_view(request):
    data = '<html><body><h1>Hello, world</h1></body></html>'
    return Response(data)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# 还不是很懂以下两个类属性
class EventViewSet(ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = EventSerializer


class Event1ViewSet(ModelViewSet):
    queryset = Event1.objects.all()
    serializer_class = Event1Serializer


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class TrackViewSet(ModelViewSet):  # V
    queryset = Track.objects.all()  # M
    serializer_class = TrackSerializer  # S
