from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name = 'home-page'),
    path('coffee/', views.coffee, name = 'coffee-page'),
    path('logout/', views.logout, name = 'logout-page'),
    path('login/', views.login, name = 'login-page'),
    path('register/', views.register, name = 'register-page'),
]
