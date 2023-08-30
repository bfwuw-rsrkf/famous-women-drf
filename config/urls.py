from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('women/', include('women.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# refresh
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzQ3ODE4NywiaWF0IjoxNjkzMzkxNzg3LCJqdGkiOiIyYTZkZTBiMTU3YzI0NDMwYWQzOThlZGUyMGExYzU3YiIsInVzZXJfaWQiOjJ9.n5eo2Nv3I_LnklINQQGkIg6C12Sz9TBY1SWqq70C-_4

# access
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzMzkyMDg3LCJpYXQiOjE2OTMzOTE3ODcsImp0aSI6ImMyMjAyNzRiNWM2MjRkNWQ5YTgwMTA5YjIzMTljMjNkIiwidXNlcl9pZCI6Mn0.WRxednpyITS3JiR6kkDqycVAp3viRJeMZJdBGgn5GFk
