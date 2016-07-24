from django.shortcuts import render
from django.http import JsonResponse
from models import Game

game = Game()


def home_page(request):
    winner = request.POST.get('winner', '')
    if winner == '':
        return render(request, 'base.html')
    else:
        return render(request, 'winner.html', {'winner': winner})


def game_screen(request):
    return render(request, 'game.html')


def game_over(request):
    #if request.method == 'POST':
    #    winner = request.POST.get('winner', '')
    #    losers = request.POST.get('losers', '')
    #    return JsonResponse({'winner': winner, 'losers': losers})
    return render(request, 'game_over.html')


def update_screen(request, json_data):
    if request.method == 'POST':
        return JsonResponse({'data': json_data})


def player_move(request, player_name):
    if player_name == 'Player 1':
        game.player_1.move()
        if game.location == game.player_1.location:
            game.winner = game.player_1
            game.end_game()
            game_over()
    else:
        game.player_2.move()
        if game.location == game.player_2.location:
            game.winner = game.player_2
            game.end_game()
            game_over()


def player_stop(request, player_name):
    if player_name == 'Player 1':
        game.player_1.pause()
    else:
        game.player_2.pause()