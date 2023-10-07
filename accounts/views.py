from django.shortcuts import render, redirect
from .form import UserForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials!')
            return redirect('login')
    else:
        pass
    return render(request, 'login.html')


def register(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = form.save(commit=False)
            user.set_password(password)
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('register')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def logout(request):
    auth.logout(request)
    messages.info(request, 'Your are logged out')
    return redirect('login')