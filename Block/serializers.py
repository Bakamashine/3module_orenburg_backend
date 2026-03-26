from rest_framework import serializers

from Block.models import Block, Room
from Block.validatiors import check_is_exists_room


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id']

class CreateBlockSerializer(serializers.Serializer):
    type = serializers.CharField(default='rectangle')
    room_id = serializers.IntegerField(validators=[check_is_exists_room])