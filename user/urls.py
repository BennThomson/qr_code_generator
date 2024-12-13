from django.urls import path
from .views import sign_up_view, login_view, logout_view, contact_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', sign_up_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
]