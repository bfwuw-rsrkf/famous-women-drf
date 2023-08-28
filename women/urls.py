from django.urls import path, include
from .views import *

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    # path('woman-create/', WomanCreateAPIView.as_view(), name='woman-post'),
    # path('woman-list/', WomanListAPIView.as_view(), name='woman-get'),
    # path('woman-update/<int:pk>/', WomanUpdateAPIView.as_view(), name='woman-put'),
    # path('woman-destroy/<int:pk>/', WomanDestroyAPIView.as_view(), name='woman-delete'),
    path('woman-list/', WomanListCreateAPIView.as_view(), name='woman-list-create'),
    path('woman-list/<int:pk>/', WomanRetrieveUpdateDestroyView.as_view(), name='woman-retr-upd-destr')
]
