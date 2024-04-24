from typing import Any
from django.utils import timezone
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Message, Room
import json

def chat(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

def send_message(request, pk):
    msg = json.loads(request.body)['message']
    room = Room.objects.get(id=pk)
    new_msg = Message.objects.create(user=request.user, text=msg)
    room.messages.add(new_msg)
    return render(request, 'chat/chat-message.html', {'m': new_msg})


class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context