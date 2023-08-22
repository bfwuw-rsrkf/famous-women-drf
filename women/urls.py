from django.urls import path
from .views import *

urlpatterns = [
    path('woman-list/', WomanListAPIView.as_view(), name='woman-list'),
]
