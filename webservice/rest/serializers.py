from rest_framework import serializers
from .models import Faculty, School, Section

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name', 'description', 'status', 'created_date', 'deleted_date')

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'description', 'status', 'created_date', 'deleted_date', 'fk_faculty')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'status', 'uc', 'semester','tipo','ht','hp','hl','created_date', 'deleted_date', 'fk_school')
