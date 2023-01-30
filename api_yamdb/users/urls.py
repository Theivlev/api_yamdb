from django.urls import path

from .views import signup, token


app_name = 'users'

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('token/', token, name='token'),
]
