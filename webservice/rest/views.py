from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import FacultySerializer, SchoolSerializer, SectionSerializer, PersonSerializer, EnrollmentSerializer
from .models import Faculty, School, Section, Person, Enrollment
from django.utils.timezone import now
from rest_framework.decorators import permission_classes
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(method='get', operation_description='Obtener un listado de todas las facultades')
@swagger_auto_schema(method='post', request_body=FacultySerializer, operation_description='Para insertar solo necesita los atributos name y description, el resto puede eliminarlos')
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

@swagger_auto_schema(method='get', operation_description='Obtener una facultad en específico')
@swagger_auto_schema(method='put', request_body=FacultySerializer, operation_description='Para modificar solo necesita los atributos id, name y description, el resto puede eliminarlos')
@swagger_auto_schema(method='delete', operation_description='Eliminar una facultad')
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

@swagger_auto_schema(method='get', operation_description='Obtener un listado de todas las escuelas')
@swagger_auto_schema(method='post', request_body=SchoolSerializer, operation_description='Para insertar solo necesita los atributos name, description y fk_faculty, el resto puede eliminarlos')
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

@swagger_auto_schema(method='get', operation_description='Obtener una escuela en específico')
@swagger_auto_schema(method='put', request_body=SchoolSerializer, operation_description='Para modificar solo necesita los atributos id, name, description y fk_faculty, el resto puede eliminarlos')
@swagger_auto_schema(method='delete', operation_description='Eliminar una escuela')
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
        serializer = SchoolSerializer(school, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.status = 'disabled'
        school.deleted_date = now()
        school.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', operation_description='Obtener un listado de todas las secciones')
@swagger_auto_schema(method='post', request_body=SectionSerializer, operation_description='Para insertar solo necesita los atributos name, description, uc, semestre, tipo, hp, ht, hl y fk_school, el resto puede eliminarlos')
@api_view(['GET', 'POST'])
def section_list(request):
    """
    Lista todas las secciones o crea una nueva seccion para una escuela
    """
    if request.method == 'GET':
        sections = Section.objects.filter(status='enabled')
        serializer = SectionSerializer(sections, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', operation_description='Obtener una seccion en específico')
@swagger_auto_schema(method='put', request_body=SectionSerializer, operation_description='Para modificar solo necesita los atributos id, name, description, uc, semestre, tipo, hp, ht, hl y fk_school, el resto puede eliminarlos')
@swagger_auto_schema(method='delete', operation_description='Eliminar una seccion')
@api_view(['GET', 'PUT', 'DELETE'])
def section_detail(request, id):
    """
    Listar, modificar o eliminar una seccion por ID
    """
    try:
        section = Section.objects.get(id=id, status='enabled')
    except Section.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = SectionSerializer(section)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SectionSerializer(section, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        section.status = 'disabled'
        section.deleted_date = now()
        section.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', operation_description='Obtener los alumnos de una seccion en específico')
@api_view(['GET'])
def section_students(request, id):
    """
    Listar los estudiantes de una seccion
    """
    try:
        section = Section.objects.get(id=id, status='enabled') 
    except Section.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fk_person = []
        enrollment = Enrollment.objects.filter(fk_section_id=section.id, status='enabled', tipo='student').values('fk_person_id')
        for e in enrollment:
            fk_person.append(e['fk_person_id'])
        fk_person.append(' ')
        people = Person.objects.raw(f'SELECT * FROM rest_person WHERE status = "enabled" and id IN {tuple(fk_person)}')
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='get', operation_description='Obtener los profesores de una seccion en específico')
@api_view(['GET'])
def section_teacher(request, id):
    """
    Listar los profesores de una seccion
    """
    try:
        section = Section.objects.get(id=id, status='enabled') 
    except Section.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        fk_person = []
        enrollment = Enrollment.objects.filter(fk_section_id=section.id, status='enabled', tipo='teacher').values('fk_person_id')
        for e in enrollment:
            fk_person.append(e['fk_person_id'])
        fk_person.append(' ')
        people = Person.objects.raw(f'SELECT * FROM rest_person WHERE status = "enabled" and id IN {tuple(fk_person)}')
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

@swagger_auto_schema(method='get', operation_description='Obtener un listado de todas las personas')
@swagger_auto_schema(method='post', request_body=PersonSerializer, operation_description='Para insertar solo necesita los atributos dni, first_name y last_name, el resto puede eliminarlos')
@api_view(['GET', 'POST'])
def person_list(request):
    """
    Lista todas las personas o crea una nueva persona para una escuela
    """
    if request.method == 'GET':
        people = Person.objects.filter(status='enabled')
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', operation_description='Obtener una persona en específico')
@swagger_auto_schema(method='put', request_body=PersonSerializer, operation_description='Para modificar solo necesita los atributos id, dni, first_name y last_name, el resto puede eliminarlos')
@swagger_auto_schema(method='delete', operation_description='Eliminar una persona')
@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, id):
    """
    Listar, modificar o eliminar una persona por ID
    """
    try:
        person = Person.objects.get(id=id, status='enabled')
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.status = 'disabled'
        person.deleted_date = now()
        person.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

@swagger_auto_schema(method='get', operation_description='Obtener un listado de todas las inscripciones')
@swagger_auto_schema(method='post', request_body=EnrollmentSerializer, operation_description='Para insertar solo necesita los atributos fk_person, fk_section y tipo, el resto puede eliminarlos')
@api_view(['GET', 'POST'])
def enrollment_list(request):
    """
    Lista todas las inscripciones con su profesor y alumno
    """
    if request.method == 'GET':
        enrollments = Enrollment.objects.filter(status='enabled')
        serializer = EnrollmentSerializer(enrollments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        Person = None
        enrollment = Enrollment.objects.filter(status='enabled').values('fk_person_id')
        serializer = EnrollmentSerializer(data=request.data)

        for e in enrollment:
            if e['fk_person_id'] == request.data.get('fk_person_id'):
                Person = True
        if serializer.is_valid() and Person == None:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', operation_description='Obtener una inscripcion en específico')
@swagger_auto_schema(method='put', request_body=EnrollmentSerializer, operation_description='Para modificar solo necesita los atributos id, fk_person, fk_section y tipo, el resto puede eliminarlos')
@swagger_auto_schema(method='delete', operation_description='Eliminar una inscripcion')
@api_view(['GET', 'PUT', 'DELETE'])
def enrollment_detail(request, id):
    """
    Listar, modificar o eliminar una inscripcion por ID
    """
    try:
        enrollment = Enrollment.objects.get(id=id, status='enabled')
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EnrollmentSerializer(enrollment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        Person = None
        personas = Enrollment.objects.filter(status='enabled').values('fk_person_id')
        serializer = EnrollmentSerializer(enrollment, data=request.data)

        for e in personas:
            if e['fk_person_id'] == request.data.get('fk_person_id'):
                Person = True
                
        if serializer.is_valid() and Person == None:
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        enrollment.status = 'disabled'
        enrollment.deleted_date = now()
        enrollment.save()
        return Response(status=status.HTTP_204_NO_CONTENT)