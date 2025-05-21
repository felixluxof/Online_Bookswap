from django.urls import path
from .views import index, about, faq, error, contact, login, signup

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('faq/', faq, name='faq'),
    path('error/', error, name='error'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),

]
