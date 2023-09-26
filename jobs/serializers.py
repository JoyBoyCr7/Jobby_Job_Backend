from .models import Job
from rest_framework import serializers

# Our jobSerializer
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'role', 'location', 'image', 'description', 'interest', 'aplication']