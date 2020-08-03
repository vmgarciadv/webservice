from rest_framework import viewsets
from .serializers import FacultySerializer, SchoolSerializer
from .models import Faculty, School

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all().order_by('id')
    serializer_class = FacultySerializer

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer