from django.urls import path
from .views import chat, send_message, RoomDetailView

urlpatterns = [
    path('', chat, name='chat'),
    path('<pk>', RoomDetailView.as_view(), name='room_detail'),
    path('<pk>/send', send_message, name='send_message')

]