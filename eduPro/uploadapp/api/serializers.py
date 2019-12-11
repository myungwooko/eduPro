from rest_framework import serializers
# from .models import File
from lecture.models import ImageResource


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageResource
        fields = "__all__"
