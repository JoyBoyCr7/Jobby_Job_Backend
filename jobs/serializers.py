from .models import Job
from rest_framework import serializers

# Our jobSerializer
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'role', 'location', 'brand_image', 'description', 'interest_level', 'aplication_date']