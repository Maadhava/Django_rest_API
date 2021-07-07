
from django.urls import path,include
from w_app import views
from w_app2.models import students
from w_app2.views import studentsViewset
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register('students',studentsViewset,basename='students')
urlpatterns = [
    path('', include(router.urls)),

]
