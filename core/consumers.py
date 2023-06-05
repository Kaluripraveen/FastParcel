import json

from channels.generic.websocket import WebsocketConsumer
from . import models
from asgiref.sync import async_to_sync
class JobConsumer(WebsocketConsumer):
    def connect(self):
        self.job_id = self.scope["url_route"]["kwargs"]["job_id"]
        self.job_group_name = "job_%s" % self.job_id

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.job_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.job_group_name, self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        job= text_data_json['job']
        
        # print("Job",job)
        if job.get('courier_lat') and job.get('courier_lng'):
            self.scope['user'].courier.lat = job['courier_lat']
            self.scope['user'].courier.lng = job['courier_lng']
            self.scope['user'].courier.save()
        # self.send(text_data=json.dumps({"message": message}))
        
        async_to_sync(self.channel_layer.group_send)(
            self.job_group_name, {"type": "job_update", "job": job}
        )
        
    def job_update(self,event):
        job = event['job']
        self.send(text_data=json.dumps({
            'job':job
        }))