from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from models import Player, Game


def home_page(request):
    winner = request.POST.get('winner', '')
    if winner == '':
        #game = Game()
        return render(request, 'base.html')
    else:
        return render(request, 'winner.html', {'winner': winner})


def game_over(request):
    if request.method == 'POST':
        winner = request.POST.get('winner', '')
        losers = request.POST.get('losers', '')
        return JsonResponse({'winner': winner, 'losers': losers})
    return render(request, 'game_over.html')