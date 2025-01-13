from django.contrib import admin
from django.urls import path, include
from .views import HomeView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', HomeView.as_view(), name='home'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
