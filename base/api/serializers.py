'''
    Serializers are basically classes they are very similar to Django Form class
    They convert the Python object into JSON format
'''
from rest_framework.serializers import ModelSerializer
from base.models import Room

class RoomSerializer(ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'