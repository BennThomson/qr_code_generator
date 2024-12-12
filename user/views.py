from django.shortcuts import render, redirect
from .forms import CustomUserLoginForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = CustomUserLoginForm()
    print('here it is!')
    if request.method == "POST":
        print('here it is is is is')
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            new_form = form.cleaned_data
            user = authenticate(email=new_form["email"], password=new_form["password"])
            print(user, '*' * 10)
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