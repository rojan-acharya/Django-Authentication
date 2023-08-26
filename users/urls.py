from django.urls import path
from .views import *

urlpatterns = [
    path('', signup_page, name='signup-page'),
    path('login/', login_page, name='login-page'),
    path('logout/', logout_page, name='logout-page'),
    path('home/', landing, name='landing-page'),
]
