from django.contrib import admin
from django.urls import path, include 
from chat import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')), 
    path('', views.home, name='home'),  
    path('accounts/login/', auth_views.LoginView.as_view(template_name='chat/login.html'), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
]
