from rest_framework.serializers import ModelSerializer
from base.models import Room, Topic
from django.contrib.auth.models import User


class TopicSerializer(ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


#nested serializer
class RoomSerializer(ModelSerializer):
    topic = TopicSerializer(many=False, read_only=True)
    host = UserSerializer(many=False, read_only=True)
    participants = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Room
        fields = '__all__'        