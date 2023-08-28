from rest_framework.serializers import ModelSerializer
from .models import Woman


class WomanSerializer(ModelSerializer):
    class Meta:
        model = Woman
        fields = [
            'title',
            'content',
            'cat'
        ]
