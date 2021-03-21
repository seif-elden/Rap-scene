# chat/consumers.py
# chat/consumers.py
import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from django.contrib.auth.models import User
from .models import Message

from django.contrib.sessions.models import Session

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'chat_chat'

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        sessionKey = text_data_json['sessionKey']
        s = Session.objects.get(session_key=sessionKey)
        user_id = s.get_decoded().get("_auth_user_id")
        user = User.objects.get(pk=user_id)
        x = Message.objects.create(
            author=user,
            content=message
        )

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message ,
                "author" : str(x.author),
                
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        author = event['author']

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            "author" : author,
        }))





