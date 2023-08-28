from django.urls import path
from .views import *

urlpatterns = [
    path('woman-create/', WomanCreateAPIView.as_view(), name='woman-post'),
    path('woman-list/', WomanListAPIView.as_view(), name='woman-get'),
    path('woman-update/<int:pk>/', WomanUpdateAPIView.as_view(), name='woman-put'),
    path('woman-destroy/<int:pk>/', WomanDestroyAPIView.as_view(), name='woman-delete')
]
