import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from asgiref.sync import async_to_sync
from django.contrib.auth.models import User

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json['message']
            sender = text_data_json['sender']
            recipient = text_data_json['recipient']
  
           
            user_sender = User.objects.get(username=sender)
            user_recipient = User.objects.get(username=recipient)

            new_message = Message.objects.create(
                user=user_sender,
                recipient=user_recipient,
                content=message
            ) 

            
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': message,
                    'sender': sender,
                    'recipient': recipient,
                }
            )
        except KeyError as e:
           
            await self.send(text_data=json.dumps({
                'error': f"Missing key in data: {str(e)}"
            }))
        except User.DoesNotExist as e:
            
            await self.send(text_data=json.dumps({
                'error': f"User not found: {str(e)}"
            }))

    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        recipient = event['recipient']

        
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender,
            'recipient': recipient,
        }))
