from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm, CustomUserCreationForm, CustomContactForm
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    form = CustomUserLoginForm()
    if request.method == "POST":
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            new_form = form.cleaned_data
            user = authenticate(email=new_form["email"], password=new_form["password"])
            if user:
                login(request, user)
                return redirect("home")
            else:
                message = "Invalid credentials"
                return render(
                    request,
                    "login.html",
                    {"form": form, "message": message},
                )
    context = {"form": form}
    return render(request, 'login.html', context)


def sign_up_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            return redirect("login")
    context = {"form": form}
    return render(request, 'signIN.html', context)


def logout_view(request):
    logout(request)
    return redirect("login")


def contact_view(request):
    form = CustomContactForm()
    if request.method == "POST":
        form = CustomContactForm(request.POST)
        if form.is_valid():
            new_form = form.cleaned_data
            form.save()
            return redirect("contact")
    context = {"form": form}
    return render(request, 'contact.html', context)