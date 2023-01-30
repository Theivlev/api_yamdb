from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from api.v1.validators import UnicodeUsernameValidator, username
from reviews.models import User


class SignUpSerializer(serializers.Serializer):
    email = serializers.EmailField(
        required=True, max_length=150)
    username = serializers.CharField(max_length=150,
                                     validators=[UnicodeUsernameValidator()],
                                     required=True)

    def validate_username(self, value):
        return username(value)


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')


class UserAdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=User.objects.all()),
            UnicodeUsernameValidator(),],
        required=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')

    def validate_username(self, value):
        return username(value)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.RegexField(
        r'^[\w.@+-]+$',
        max_length=150,
        required=True)
    email = serializers.EmailField(max_length=150, required=True)
    role = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role')
