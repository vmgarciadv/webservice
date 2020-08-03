from rest_framework import viewsets
from .serializers import FacultySerializer
from .models import Faculty

class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all().order_by('id')
    serializer_class = FacultySerializer