from rest_framework import serializers
from .models import Category, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'views']
        extra_kwargs = {
            'title': {'max_length': 100},
            'content': {'max_length': 5000},
        }