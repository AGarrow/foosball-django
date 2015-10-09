from django.db import models
from django.db.models.signals import post_save
class Player(models.Model):
  name = models.CharField(max_length=40)
  wins = models.IntegerField(default=0)
  losses = models.IntegerField(default=0)
  goals = models.IntegerField(default=0)
  goals_against = models.IntegerField(default=0)
  win_percentage = models.FloatField(default=0.0)
  goal_ratio = models.FloatField(default=0.0)

  def __unicode__(self):
    return self.name

  def update_player_info(self):

    wins = Game.objects.filter(winner=self)
    losses = Game.objects.filter(loser=self)
    
    self.wins = wins.count()    
    self.losses = losses.count()
    

    loss_goals = 0
    for loss in losses:
      goals = loss.silver_score if loss.silver_score < 10 else loss.black_score
      loss_goals += goals
    self.goals = (self.wins * 10) + loss_goals

    win_goals_against = 0
    for win in wins:
      goals = win.silver_score if win.silver_score < 10 else win.black_score
      win_goals_against += goals
    self.goals_against = (self.losses * 10) + win_goals_against

    self.win_percentage = float(self.wins) / float(self.losses) if self.losses > 0 else 1.0
    self.goal_ratio = float(self.goals) / float(self.goals_against)

    self.save()


class Game(models.Model):
  black = models.ForeignKey(Player, related_name="black_player", verbose_name="Black Player")
  silver = models.ForeignKey(Player, related_name="silver_player", verbose_name="Silver Player")
  winner = models.ForeignKey(Player, related_name="winner", verbose_name="the winner of the game")
  loser = models.ForeignKey(Player, related_name="loser", verbose_name="loser of the game", null=True)
  black_score = models.IntegerField(default=0)
  silver_score = models.IntegerField(default=0)
  complete = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return str({"black": self.black.name, "silver": self.silver.name, "score": {"black": self.black_score, "silver":self.silver_score} })

def update_standings_info(sender, instance, created, **kwargs):
  for p in Player.objects.all():
    p.update_player_info()

post_save.connect(update_standings_info, sender=Game)
