from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

from Block.models import Block, Room, ShareRoom
from Block.serializers import BlockSerializer, ListRoomSerializer, CreateBlockSerializer, CreateRoomSerializer, \
    ShareRoomSerializer


# Create your views here.
class BlockViewApi(generics.ListCreateAPIView):
    # serializer_class = CreateBlock
    queryset = Block.objects.all()

    created_object = None

    def get_serializer_class(self):
        if self.request.method == "POST":
            return CreateBlockSerializer
        return BlockSerializer

    def perform_create(self, serializer):
        validated_data = serializer.validated_data
        block = Block.objects.create(
            x=100,
            y=100,
            width=100,
            height=100,
            color='red',
            room_id=validated_data['room_id']
        )
        self.created_object = block

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        output_serializer = BlockSerializer(self.created_object)
        headers = self.get_success_headers(output_serializer.data)
        return Response(output_serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class RoomViewApi(generics.ListCreateAPIView):
    queryset = Room.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return CreateRoomSerializer
        return ListRoomSerializer

    def get_permissions(self):
        if self.request.method == "POST":
            return (IsAuthenticated(),)
        return (AllowAny(),)

    def perform_create(self, serializer):
        Room.objects.create(
            user_id=self.request.user.id
        )


class PrivateRoomApi(generics.ListAPIView):
    serializer_class = ListRoomSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Room.objects.filter(status=Room.EncapsulationOfRooms.PRIVATE)


class ShareRoomApi(generics.CreateAPIView):
    serializer_class = ShareRoomSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        ser_result = self.serializer_class(data=self.request.data)
        if ser_result.is_valid():
            to_user_id = ser_result['to_user']
            room_id = ser_result['room_id']
            ShareRoom.objects.create(
                user_id=request.user.id,
                to_user=to_user_id,
                room_id=room_id
            )
            return Response(status=HTTP_201_CREATED)
        return Response(ser_result.data, status=422)
    # def create(self, request, *args, **kwargs):
    #     validated_data = self.serializer_class(data=self.request.data)
    #     ShareRoom.objects.create(
    #         user_id = request.user.id,
    #         to_user=validated_data['to_user'],
    #         room_id=validated_data['room']
    #     )
