from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Room, Message
from .forms import MessageForm

from .models import Room, Message
from .forms import CreateRoomForm  

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required
def room_with_messages(request, slug):
    room = get_object_or_404(Room, slug=slug)
    messages = Message.objects.filter(room=room).order_by('date_added')

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()
    else:
        form = MessageForm()

    return render(request, 'room_with_messages.html', {'room': room, 'messages': messages, 'form': form})

@login_required
def create_room(request):
    if request.method == 'POST':
        form = CreateRoomForm(request.POST)
        if form.is_valid():
            room = form.save(commit=False)
            room.created_by = request.user
            room.save()
            messages.success(request, 'Room created successfully.')
            return redirect('rooms')
    else:
        form = CreateRoomForm()

    return render(request, 'room/create_room.html', {'form': form})

def create_room(request):
    
    return render(request, 'room/create_room.html')