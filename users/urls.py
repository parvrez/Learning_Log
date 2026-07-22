'''from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path=('',include('django.contrib.auth.urls')),
   
]'''



#from django.contrib import admin
from django.urls import path, include

from .import views
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    
]


''' path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),'''
