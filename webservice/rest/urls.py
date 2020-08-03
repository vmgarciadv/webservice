from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'schools', views.SchoolViewSet)
router.register(r'sections', views.SectionViewSet)
router.register(r'people', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('faculties/', views.faculty_list),
    path('faculties/<int:id>/', views.faculty_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]