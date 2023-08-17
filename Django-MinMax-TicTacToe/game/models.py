from django.db import models

# Create your models here.

class Game(models.Model):
    room_code = models.CharField(max_length=10)
    game_creator = models.CharField(max_length=10)
    game_oppenent = models.CharField(max_length=10 , blank=True , null=True)
    is_over = models.BooleanField(default=False)

    def __str__(self):
        return self.room_code
