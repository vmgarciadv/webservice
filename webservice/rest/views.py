from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FacultySerializer, SchoolSerializer, SectionSerializer, PersonSerializer
from .models import Faculty, School, Section, Person
from django.utils.timezone import now

@api_view(['GET', 'POST'])
def faculty_list(request):
    """
    Lista todas las facultades o crea una nueva facultad
    """
    if request.method == 'GET':
        faculties = Faculty.objects.filter(status='enabled')
        serializer = FacultySerializer(faculties, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FacultySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def faculty_detail(request, id):
    """
    Listar, modificar o eliminar una facultad por ID
    """
    try:
        faculty = Faculty.objects.get(id=id, status='enabled')
    except Faculty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = FacultySerializer(faculty)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = FacultySerializer(faculty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        faculty.status = 'disabled'
        faculty.deleted_date = now()
        faculty.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def school_list(request):
    """
    Lista todas las escuelas o crea una nueva escuela para una facultad
    """
    if request.method == 'GET':
        schools = School.objects.filter(status='enabled')
        serializer = SchoolSerializer(schools, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def school_detail(request, id):
    """
    Listar, modificar o eliminar una escuela por ID
    """
    try:
        school = School.objects.get(id=id, status='enabled')
    except School.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SchoolSerializer(school)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SchoolSerializer(School, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.status = 'disabled'
        school.deleted_date = now()
        school.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SectionViewSet(viewsets.ModelViewSet):
    queryset = Section.objects.all()
    serializer_class = SectionSerializer

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer