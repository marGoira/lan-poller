from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vote(models.Model):
    game_order = models.JSONField(default=list)

    def __str__(self):
        return str(self.game_order)
