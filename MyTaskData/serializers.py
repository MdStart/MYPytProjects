from rest_framework import serializers

from .models import MyData


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyData
        fields = ('device_name', 'magnification', 'field_of_view', 'range')
