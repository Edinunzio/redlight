from django.shortcuts import render
from django.http import HttpResponse
from models import Player, Game


def home_page(request):
    player = request.POST.get('winner', '')
    if player == '':
        return render(request, 'base.html')
    else:
        return render(request, 'winner.html', {'player': player})
