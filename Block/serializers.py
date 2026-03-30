from rest_framework import serializers

from Block.models import Block, Room, ShareRoom
from Block.validatiors import check_is_exists_room


class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = '__all__'


class ListRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id']


class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = []


class CreateBlockSerializer(serializers.Serializer):
    type = serializers.CharField(default='rectangle')
    room_id = serializers.IntegerField(validators=[check_is_exists_room])


class ShareRoomSerializer(serializers.ModelSerializer):
    # to_user = serializers.CharField(validators=[lambda value: get_object_or_404(get_user_model(), pk=value)])
    class Meta:
        model = ShareRoom
        fields = ["to_user", "room"]
