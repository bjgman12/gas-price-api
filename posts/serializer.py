from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ( 'id', 'author', 'station' , 'price' , 'created_at')
        model = Posts