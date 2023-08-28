from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from .models import Woman
from .serializers import WomanSerializer


class WomanCreateAPIView(CreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanListAPIView(ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanUpdateAPIView(UpdateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


class WomanDestroyAPIView(DestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
