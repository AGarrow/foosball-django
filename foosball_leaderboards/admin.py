from django.contrib import admin

# Register your models here.
from .models import *
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
  def __str__():
    self.name
  pass

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
  pass