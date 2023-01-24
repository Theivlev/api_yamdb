from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoryViewSet,
                    GenreViewSet,
                    TitleViewSet,
                    ReviewViewSet,
                    token,
                    signup,)

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register('titles', TitleViewSet, basename='title')
router_v1.register('categories', CategoryViewSet, basename='category')
router_v1.register('genres', GenreViewSet, basename='genre')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/auth/', include('djoser.urls')),
    path('v1/auth/', include('djoser.urls.jwt')),
    path('v1/auth/signup/', signup, name='signup'),
    path('v1/auth/token/', token, name='token'),
]