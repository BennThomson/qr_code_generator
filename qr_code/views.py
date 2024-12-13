from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import os
import qrcode

def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')


def qr_code_view(request):
    return render(request, 'qrCode.html')

