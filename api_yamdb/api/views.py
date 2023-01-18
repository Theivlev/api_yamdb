from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from reviews.models import Category, Genre, Title
from .serializers import (
    CategorySerializer,
    GenreSerializer,
    TitleSerializer,
    ReviewSerializer,
    MyTokenObtainPairSerializer
)



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # permission_classes =
    filter_backends = (SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(viewsets.ModelViewSet):
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


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    # permission_classes =

    def get_title(self):
        title_id = self.kwargs['title_id']
        return get_object_or_404(Title, id=title_id)

    def get_queryset(self):
        title = self.get_title()
        return title.reviews.all()

    def perform_create(self, serializer):
        title = self.get_title()
        serializer.save(author=self.request.user, title=title)

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer