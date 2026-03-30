from django.urls import path

from .views import BlockViewApi, RoomViewApi, PrivateRoomApi, ShareRoomApi

urlpatterns = [
    path('api/block/', BlockViewApi.as_view()),
    path('api/room/', RoomViewApi.as_view()),
    path("api/private/room", PrivateRoomApi.as_view()),
    path("api/share/room", ShareRoomApi.as_view())
]
