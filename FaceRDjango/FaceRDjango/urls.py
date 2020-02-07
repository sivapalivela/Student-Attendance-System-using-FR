from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from AppFR1.views import UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

router = routers.DefaultRouter()
router.register('users',UserViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
    path('appfr1/',include('AppFR1.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]