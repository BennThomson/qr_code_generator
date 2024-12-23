from django.urls import path
from .views import home, about_view, qr_code_view

urlpatterns = [
    path('', home, name='home'),
    path('about/', about_view, name='about'),
    path('qr_code/', qr_code_view, name='QRcode'),
]
