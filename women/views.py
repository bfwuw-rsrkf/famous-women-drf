from rest_framework import generics
from .models import Woman
from .serializers import WomanSerializer


class WomanListAPIView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
