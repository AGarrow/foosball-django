from django.http import HttpResponse
from django.shortcuts import render
from models import Player, Game

# Create your views here.
def home(request):
    context = {
      "players" : Player.objects.order_by('-goal_ratio'),
      "games" : Game.objects.order_by('-created_at')
    }

    return HttpResponse(render(request, "home.html", context=context))