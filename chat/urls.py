from django.urls import path
from .views import chat, send_message, create_room, RoomDetailView

urlpatterns = [
    path('', chat, name='chat'),
    path('create-room', create_room, name='create_room'),
    path('<pk>', RoomDetailView.as_view(), name='room_detail'),
    path('<pk>/send', send_message, name='send_message'),

]