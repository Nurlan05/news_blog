from rest_framework import serializers
from mainapp.models import News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields='__all__'

class NewsCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','title','content']