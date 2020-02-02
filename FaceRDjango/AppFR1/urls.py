from django.urls import path,include
from AppFR1 import views
from rest_framework.urlpatterns import format_suffix_patterns
#added from here
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

#till here
urlpatterns = [
    path('api/students/add',views.AddStudents.as_view()),
    path('api/students/view',views.ProcessStudents.as_view()),
    path('api/students/addbranch',views.AddBranche.as_view()),
    path('api/students/addstudyingyear',views.AddStudyingYear.as_view()),
    path('api/students/addsection',views.AddSection.as_view()),
    path('api/', include(router.urls)),
    path('auth/', ObtainAuthToken.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)