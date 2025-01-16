from django.urls import path
from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.chat, name='chat'),
    path('messages/<int:receiver_id>/', views.get_messages, name='get_messages'),
]
