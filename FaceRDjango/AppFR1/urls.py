from django.urls import path,include
from AppFR1 import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/students/add',views.AddStudents.as_view()),
    path('api/students/view',views.ProcessStudents.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)