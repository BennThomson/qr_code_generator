from django.urls import path
from .views import login, sign_up_view

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', sign_up_view, name='register'),
]