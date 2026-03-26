from django.urls import path, include
from .views import BlockViewApi, RoomViewApi

urlpatterns = [
    path('api/block/', BlockViewApi.as_view()),
    path('api/room/', RoomViewApi.as_view())
]