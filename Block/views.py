from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import generics, response, status
from rest_framework.response import Response

from Block.models import Block, Room
from Block.serializers import BlockSerializer, RoomSerializer, CreateBlockSerializer


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

class RoomViewApi(generics.ListAPIView):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()
