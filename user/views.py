from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def sign_up_view(request):
    return render(request, 'signIN.html')
