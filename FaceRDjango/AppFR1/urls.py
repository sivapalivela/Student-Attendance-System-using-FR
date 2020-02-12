from django.urls import path,include
from AppFR1 import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('api/students/add_student',views.AddStudent.as_view()),
    path('api/students/take_attendance',views.AddAttendance.as_view()),
    path('api/students/add_class',views.Allocate_Classes.as_view()),
    path('api/students/getallocatedclass',views.GetAllocatedClasses.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = format_suffix_patterns(urlpatterns)