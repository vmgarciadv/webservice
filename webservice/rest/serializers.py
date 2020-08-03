from rest_framework import serializers
from .models import Faculty

class FacultySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Faculty
        fields = ('id', 'name', 'description', 'status', 'created_date', 'deleted_date')
