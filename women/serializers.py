from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from .models import Woman
# import io


# class WomanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Woman
#         fields = [
#             'title',
#             'content',
#             'cat'
#         ]


class WomanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_created = serializers.DateField(read_only=True)
    time_updated = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=False)
    cat_id = serializers.IntegerField()

    def create(self, validated_data):
        return Woman.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance
