from .models import Job
from rest_framework import serializers

# Our jobSerializer
class JobSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Job
        fields = ['id', 'role', 'location', 'description', 'interest_level', 'application_date']
# removed  'brand_image'