from rest_framework import serializers
from todo.models import Task
from django.contrib.auth import get_user_model

user = get_user_model()

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'user', 'title', 'complete', 'created_date']
        read_only_fieldss = ['user']
    
    def create(self, validated_data):
        validated_data['user'] = user.objects.get(id = self.context.get('request').id)
        return super().create(validated_data)
    