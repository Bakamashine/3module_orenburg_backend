from django.db import models
from django.db.models import CASCADE


class Room(models.Model):
    status = models.BooleanField(verbose_name="Открытость", default=1)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Комната"
        verbose_name_plural = "Комнаты"

class Block(models.Model):
    room = models.ForeignKey(to=Room, on_delete=CASCADE)
    x = models.IntegerField(verbose_name="Место по оси x")
    y = models.IntegerField(verbose_name='Место по оси Y')
    width = models.IntegerField(verbose_name="Длина")
    height = models.IntegerField(verbose_name="Высота")
    color = models.CharField(verbose_name="Цвет")


    def __str__(self):
        return str(self.id)
    class Meta:
        verbose_name = "Блок"
        verbose_name_plural = "Блоки"