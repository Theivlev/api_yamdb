from rest_framework import serializers
from reviews.models import Category, Genre, Title, Review, Comment
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from reviews.models import User
from rest_framework.validators import UniqueValidator
from django.db.models import Avg
from rest_framework.validators import UniqueTogetherValidator
from users.models import CustomUser
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'slug')
        model = Genre


class TitleSerializerCreate(serializers.ModelSerializer):
    """Для создания"""
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

class TitleSerializerRead(serializers.ModelSerializer):
    """Для чтения"""
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'description', 'year', 'category', 'genre', 'rating'
        )
        read_only_fields = ('id',)

    def get_rating(self, obj):
        obj = obj.reviews.all().aggregate(rating=Avg('score'))
        return obj['rating']

class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')
    title = serializers.PrimaryKeyRelatedField(read_only=True)
    score = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        fields = '__all__'
        model = Review

    def create(self, validated_data):
        if Review.objects.filter(
            author=validated_data['author'], title=validated_data['title']
        ).exists():
            raise serializers.ValidationError(
                'Можно оставить только один отзыв на произведение.')
        review = Review.objects.create(**validated_data)
        return review
from api.validators import UnicodeUsernameValidator
class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all()), UnicodeUsernameValidator()],
        required=True,
    )

    def create(self, validated_data):
        return User.objects.create(**validated_data)
        
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Недопустимое имя пользователя')
        return value

class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(r'^[\w.@+-]+$', max_length=150, required=True)
    email = serializers.EmailField(max_length=150, required=True)
    role = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = User
        fields = '__all__'

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError('Недопустимое имя пользователя')
        return value

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    review = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'

class UserAdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all()), UnicodeUsernameValidator()],
        required=True,
    )
    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError(
                'Имя пользователя "me" не разрешено.'
            )

