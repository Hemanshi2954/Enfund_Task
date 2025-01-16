from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('chat')
    else:
        form = UserCreationForm()
    return render(request, 'chat/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('chat')
    return render(request, 'chat/login.html')

@login_required
def chat(request, username):
    other_user = User.objects.get(username=username)
    messages = Message.objects.filter(
        sender=request.user, receiver=other_user
    ) | Message.objects.filter(
        sender=other_user, receiver=request.user
    ).order_by('timestamp')
    return render(request, 'chat/chat.html', {'messages': messages, 'other_user': other_user})

@login_required
def get_messages(request, receiver_id):
    messages = Message.objects.filter(sender=request.user, receiver_id=receiver_id) | \
              Message.objects.filter(sender_id=receiver_id, receiver=request.user)
    return render(request, 'chat/messages.html', {'messages': messages, 'receiver_id': receiver_id})

# @login_required
def home(request):
    return render(request, 'chat/home.html')