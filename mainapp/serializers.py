from rest_framework import serializers
from mainapp.models import News

class NewsSerializers(serializers.ModelSerializer):
    class Meta:
        model=News
        fields=['id','title','content']