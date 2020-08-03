from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('faculties/', views.faculty_list),
    path('faculties/<int:id>/', views.faculty_detail),
    path('schools/', views.school_list),
    path('schools/<int:id>/', views.school_detail),
    path('sections/', views.section_list),
    path('sections/<int:id>/', views.section_detail),
    path('people/', views.person_list),
    path('people/<int:id>/', views.person_detail),
    path('enrollments/', views.enrollment_list),
    path('enrollments/<int:id>/', views.enrollment_detail),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]