from django.urls import path
from .views import *

urlpatterns = [
    path('woman-list/', WomanListCreateAPIView.as_view(), name='woman-list-create'),
    path('woman-list/<int:pk>/', WomanRetrieveUpdateDestroyView.as_view(), name='woman-retr-upd-destr'),
]
