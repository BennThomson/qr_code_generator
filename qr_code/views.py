from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def qr_code_view(request):
    return render(request, 'qrCode.html')

