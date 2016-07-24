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


def update_screen(request, json_data):
    if request.method == 'POST':
        return JsonResponse({'data': json_data})


def player_move(request, player_name):
    if game.light_color == 'red':
        game.losers.append(player_name)
    else:
        if player_name == "1":
            game.player_1.move()
            if game.player_1.location == game.distance:
                game.winner = game.player_1
                game.end_game()
                return render(request, 'game_over.html')
        else:
            game.player_2.move()
            if game.distance == game.player_2.location:
                game.winner = game.player_2
                game.end_game()
                return render(request, 'game_over.html')
    return render(request, 'game.html')
    #return JsonResponse({'data': data})
