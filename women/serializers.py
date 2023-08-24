from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from .models import Woman
# import io


# class WomanSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Woman
#         fields = [
#             'id',
#             'title',
#             'content',
#         ]


# class WomanModel:
#     def __init__(self, title, content, is_published):
#         self.title = title
#         self.content = content
#         self.is_published = is_published
#
#
# class WomanSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     is_published = serializers.BooleanField(default=False)
#
#
# def encode():
#     model = WomanModel('Ainazik Paizullaeva', 'Ноутбук алды', True)
#     model_sr = WomanSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
#
# def decode():
#     unb = io.BytesIO(b'{"title":'
#                      b'"Ainazik Paizullaeva",'
#                      b'"content":'
#                      b'"\xd0\x9d\xd0\xbe\xd1\x83\xd1\x82\xd0\xb1\xd1\x83\xd0\xba \xd0\xb0\xd0\xbb\xd0\xb4\xd1\x8b",'
#                      b'"is_published":'
#                      b'true}')
#     data = JSONParser().parse(unbyte)
#     serializer = WomanSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)


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
