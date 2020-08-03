from rest_framework import serializers
from .models import Faculty, School, Section, Person
from django.utils.timezone import now

class FacultySerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=20, required=False)
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

class SchoolSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(max_length=30, required=False)
    status = serializers.CharField(default='enabled', max_length=10, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)
    fk_faculty_id = serializers.IntegerField(required=False)


    def create(self, validated_data):
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.fk_faculty_id = validated_data.get('fk_faculty_id', instance.fk_faculty_id)
        instance.save()
        return instance

class SectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    name = serializers.CharField(max_length=20, required=False)
    description = serializers.CharField(max_length=30, required=False)
    status = serializers.CharField(default='enabled', max_length=10, required=False)
    uc = serializers.IntegerField(required=False)
    semester = serializers.IntegerField(required=False)
    tipo = serializers.CharField(max_length=9, required=False)
    created_date = serializers.DateTimeField(default=now, required=False)
    deleted_date = serializers.DateTimeField(required=False)
    fk_school_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        return Section.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.uc = validated_data.get('uc', instance.uc)
        instance.semester = validated_data.get('semester', instance.semester)
        instance.tipo = validated_data.get('tipo', instance.tipo)
        instance.fk_school_id = validated_data.get('fk_school_id', instance.fk_school_id)
        instance.save()
        return instance

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'DNI', 'first_name', 'last_name', 'status', 'created_date', 'deleted_date')
