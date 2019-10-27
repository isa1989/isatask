import asyncio
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
from .models import Comment, Task


class CommentConsumer(AsyncConsumer):

    async def websocket_connect(self, event):
        print('connection successfull', event)
        await self.send({
            'type': 'websocket.accept',
        })

        post_id = await self.get_post_id(self.scope['url_route']['kwargs']['pk'])
        self.post = 'post_' + post_id
        await self.channel_layer.group_add(
            self.post,
            self.channel_name
        	)

    async def websocket_receive(self, event):
    	print('received:', event)
    	new_comment_data = event.get('text')
    	new_comment = json.loads(new_comment_data)
    	post_id = new_comment['post_id']
    	author = new_comment['author']
    	description = new_comment["description"]
    	await self.create_comment(post_id, author, description)
    	comment = {
    	     'description': description,
    	     'author': author
    	}
    	await self.channel_layer.group_send(
            self.post,
            {
                 'type': 'show_comment',
                 'text': json.dumps(comment)
            }            
        	)


    @database_sync_to_async
    def create_comment(self, id, user, description):
    	user = User.objects.get(username=user)
    	comm = Task.objects.get(id=id)
    	Comment.objects.create(comm=comm, user=user, description=description)


    @database_sync_to_async
    def get_post_id(self, id):
    	return str(Task.objects.get(id=id).id)


    async def show_comment(self, event):
    	await self.send({
                'type': 'websocket.send',
                'text': event['text']     
    	    })



