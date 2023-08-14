from rest_framework import serializers

from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta():
        # 메타 클래스에서 model = Task
        model = Task
        # 고유 id, 할 일, 성공 여부의 속성
        fields = ('id', 'work', 'isComplete')