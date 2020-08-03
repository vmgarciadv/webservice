from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'faculties', views.FacultyViewSet)
router.register(r'schools', views.SchoolViewSet)
router.register(r'sections', views.SectionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]