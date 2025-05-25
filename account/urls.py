from django.urls import path, include
from . import views

urlpatterns = [
    # Аутентификация: вход, выход, смена пароля и т.д.
    path('', include('django.contrib.auth.urls')),

    # Главная страница после входа
    path('', views.dashboard, name='dashboard'),

    # Страница регистрации
    path('register/', views.register, name='register'),
]
