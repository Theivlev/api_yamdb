from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
)
from .viewsets import CreateListDestroyViewSet


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = (Title.objects.all()
                .select_related('category')
                .prefetch_related('genre'))
    serializer_class = TitleSerializer
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)
