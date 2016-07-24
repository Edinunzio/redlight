from django.shortcuts import render
from django.http import HttpResponse
from models import Player, Game


def home_page(request):
    """try:
        game
    except:
        game = Game()
    """
    winner = request.POST.get('winner', '')
    if winner == '':
        return render(request, 'base.html')
    else:
        return render(request, 'winner.html', {'winner': winner})
