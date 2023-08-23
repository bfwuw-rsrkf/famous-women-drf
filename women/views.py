from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Woman
from .serializers import WomanSerializer


class WomanListAPIView(APIView):
    def get(self, request):
        posts = Woman.objects.all().values()
        return Response({'posts': posts})

    def post(self, request):
        post_new = Woman.objects.create(
            title=request.data['title'],
            content=request.data['content'],
            is_published=request.data['is_published'],
        )
        return Response({'post': post_new})


# class WomanListAPIView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
