from django.urls import path,include
from AppFR1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('api/students/add_student',views.AddStudent.as_view()),
    path('api/students/take_attendance',views.AddAttendance.as_view()),
    path('api/students/add_class',views.Allocate_Classes.as_view()),
    
    path('api/', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)