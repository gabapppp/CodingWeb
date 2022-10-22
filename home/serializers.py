from rest_framework import serializers
from base64 import urlsafe_b64decode
# from home.models import Source


class SourceSerializer(serializers.Serializer):
    language = serializers.ChoiceField(choices=(['python', 'cpp', ]), default='python')
    source_code = serializers.CharField(allow_blank=False)
    stdin = serializers.CharField(allow_blank=True)

