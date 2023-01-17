from rest_framework import serializers
from reviews.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True)

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',)

    class Meta:
        fields = '__all__'
        model = Title
