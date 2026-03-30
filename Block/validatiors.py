from django.shortcuts import get_object_or_404

from Block.models import Room


def check_is_exists_room(id: int | str):
    get_object_or_404(Room, pk=id)
