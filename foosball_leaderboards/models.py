from django.db import models

class Player(models.Model):
  name = models.CharField(max_length=40)

class Game(models.Model):
  black = models.ForeignKey(Player, related_name="black_player", verbose_name="Black Player")
  silver = models.ForeignKey(Player, related_name="silver_player", verbose_name="Silver Player")
  winner = models.ForeignKey(Player, related_name="winner", verbose_name="the winner of the game")