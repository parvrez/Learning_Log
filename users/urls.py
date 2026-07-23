from django.urls import path, include
from . import views

urlpatterns = [
    # Include default authentication URLs.
    path('', include('django.contrib.auth.urls')),

    # Registration page.
    path('register/', views.register, name='register'),
]