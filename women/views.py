from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Woman
from .pagination import PaginationWoman
from .permissions import IsOwnerOrReadOnly
from .serializers import WomanSerializer


class WomanListCreateAPIView(ListCreateAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    pagination_class = PaginationWoman
    permission_classes = (IsAuthenticatedOrReadOnly,)


class WomanRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
    pagination_class = PaginationWoman
    permission_classes = (IsOwnerOrReadOnly,)
