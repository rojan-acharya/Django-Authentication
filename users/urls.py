from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_page, name='signup-page'),
    path('login/', login_page, name='login-page'),
    path('home/', landing, name='landing-page'),
]
