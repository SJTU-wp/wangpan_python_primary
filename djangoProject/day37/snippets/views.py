from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer


@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        # serializer是一个序列化对象
        serializer = SnippetSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)  # 使用Django自带方法，响应json格式的数据

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':  # 详情页的查询
        serializer = SnippetSerializer(snippet)  # 序列化
        return JsonResponse(serializer.data)  # 使用Django自带方法，响应json格式的数据

    elif request.method == 'PUT':  # 修改
        data = JSONParser().parse(request)  # 将数据解析为Python原生数据类型
        serializer = SnippetSerializer(snippet, data=data)  # 反序列化
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':  # 删除
        snippet.delete()
        return HttpResponse(status=204)
