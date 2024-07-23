"""
URL configuration for drfsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshSlidingView

from person.views import *


# router = routers.SimpleRouter()
# router.register(r'getallpoet', ModelViewSet, basename="poet") # r - puts slash on the urls itself




urlpatterns = [
    path('admin/', admin.site.urls),
    # Session id
    path('api/v1/auth/', include('rest_framework.urls')), # authorization cookie

    # path('api/v1/', include(router.urls)),

    # path('api/v1/update/<int:pk>/', CRUDPoet.as_view({'update': 'list'})),
    path('api/v1/updatepoet/', ListCreatePoet.as_view()),
    # path('api/v1/retrivedeletepoet/<int:pk>/', DeleteRetrivePoet.as_view()),

    #Djoser
    path('api/auth/', include('djoser.urls')), #Registration
    re_path(r'^auth/', include('djoser.urls.authtoken')), #Authorization

    # JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshSlidingView.as_view(), name='token_refresh'),
]


