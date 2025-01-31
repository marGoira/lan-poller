from django.db import models

class Game(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Vote(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.game.name}: {self.votes} votes"
