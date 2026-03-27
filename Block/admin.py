from django.contrib import admin
from .models import Block, Room, ShareRoom

# Register your models here.
admin.site.register(Room)
admin.site.register(Block)
admin.site.register(ShareRoom)