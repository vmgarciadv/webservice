from rest_framework import serializers
from .models import Faculty, School, Section, Person
from django.utils.timezone import now

class FacultySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=30, required=False)
    status = serializers.CharField(default='enabled', max_length=10, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        return Faculty.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ('id', 'name', 'description', 'status', 'created_date', 'deleted_date', 'fk_faculty')

class SectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Section
        fields = ('id', 'name', 'description', 'status', 'uc', 'semester','tipo','ht','hp','hl','created_date', 'deleted_date', 'fk_school')

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'DNI', 'first_name', 'last_name', 'status', 'created_date', 'deleted_date')
