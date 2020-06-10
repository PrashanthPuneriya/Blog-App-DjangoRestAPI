from .models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('title', 'content')
        model = Post