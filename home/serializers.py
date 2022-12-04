from rest_framework import serializers
from drf_extra_fields.fields import Base64FileField
from .models import Source
from django.contrib.auth.models import User

# todo make accept a list of extensions (finite eg. )


class Base64File(Base64FileField):
    ALLOWED_TYPES = ['py', 'js', 'cpp', 'jav']

    def get_file_extension(self, filename, decoded_file):
        extension = self.get_full_name().split('.')[-1]
        return extension

    def get_file_name(self, decoded_file):
        attachment_filename = self.get_full_name()
        return '.'.join(attachment_filename.split('.')[:-1])

    def get_full_name(self):
        # todo validate name
        return self.context['request'].data['filename']


class SourceSerializer(serializers.ModelSerializer):
    file = Base64File()
    author = serializers.SlugRelatedField('username', read_only=True)

    class Meta:
        model = Source
        fields = '__all__'


class ExecuteSerializer(serializers.Serializer):
    fileID = serializers.IntegerField()
    stdin = serializers.CharField(allow_null=True)
