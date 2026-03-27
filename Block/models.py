from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

class Room(models.Model):
    class EncapsulationOfRooms(models.TextChoices):
        PUBLIC = "public"
        PROTECTED = "protected"
        PRIVATE = "private"
    user = models.ForeignKey(to=User, null=True, blank=True, default=None, on_delete=CASCADE)
    open = models.BooleanField(verbose_name="Открытость", default=True)
    status = models.CharField(max_length=20, choices=EncapsulationOfRooms.choices, default=EncapsulationOfRooms.PRIVATE)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

class ShareRoom(models.Model):
    room = models.ForeignKey(to=Room, on_delete=CASCADE, related_name='shares')
    to_user = models.ForeignKey(to=User,null=True, on_delete=models.SET_NULL, related_name='shared_rooms_received')
    user = models.ForeignKey(to=User, null=True,on_delete=models.SET_NULL, related_name='shared_rooms_sent')

    def __str__(self):
        return f"Share {self.room.id} from {self.user} to {self.to_user}"

    class Meta:
        verbose_name = "Доступ к комнате"
        verbose_name_plural = "Доступы к комнатам"

class Block(models.Model):
    room = models.ForeignKey(to=Room, on_delete=CASCADE, related_name='blocks')
    x = models.IntegerField(verbose_name="Место по оси x")
    y = models.IntegerField(verbose_name='Место по оси Y')
    width = models.IntegerField(verbose_name="Длина")
    height = models.IntegerField(verbose_name="Высота")
    color = models.CharField(verbose_name="Цвет")


    def __str__(self):
        return f"Block {self.id} in Room {self.room.id}"
    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"