from django.shortcuts import render
from django.http import HttpResponse
from models import Player, Game

def home_page(request):
    data = dict()
    data['player'] = request.POST.get('winner', '')
    if data['player'] == '':
        return render(request, 'base.html')
    else:
        return render(request, 'winner.html', {'player': data['player']})
