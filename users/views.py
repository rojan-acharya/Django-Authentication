from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login, logout

CustomUser = get_user_model()

def signup_page(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if not name or not email or not phone or not pass1 or not pass2:
            messages.error(request, 'Please fill all the fields properly!')
        elif pass1 != pass2:
            messages.error(request, "Password do not match. Please try again.")
        elif CustomUser.objects.filter(email=email).exists():
            messages.error(
                request, 'An account with this email already exists.')
        elif CustomUser.objects.filter(phone=phone).exists():
            messages.error(
                request, 'An account with this phone number already exists.')
        else:
            user = CustomUser.objects.create_user(
                name=name, email=email, phone=phone, password=pass1)
            user.save()
            messages.success(
                request, "Account created successfully. You can now log in.")
            return redirect('login-page')
    return render(request, 'signup.html')


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('landing-page')
        elif not email:
            messages.error(request, 'Email is required!')
        elif not password:
            messages.error(request, 'Password is required!')
        else:
            messages.error(
                request, 'Email or password is incorrect. Try Again!')
    return render(request, 'login.html')


def landing(request):
    return render(request, 'landing.html')