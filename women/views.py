from django.forms import model_to_dict
from rest_framework.response import Response
# from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from .models import Woman
from .serializers import WomanSerializer


class WomanListAPIView(APIView):
    def get(self, request):
        posts = Woman.objects.all()
        return Response({'posts': WomanSerializer(posts, many=True).data})

    def post(self, request):
        serializer = WomanSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method Put not allowed.'})
        try:
            instance = Woman.objects.get(pk=pk)
        except KeyError:
            return Response({'error': 'Object does not exist.'})
        serializer = WomanSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})


# class WomanListAPIView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
