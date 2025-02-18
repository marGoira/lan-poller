from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from .models import Game, Vote
import json

@csrf_protect
def poller_view(request):
    if request.method == 'POST':
        game_order_json = request.POST.get('game_order', '[]')
        game_order = json.loads(game_order_json)
        print(f"Game Order: {game_order}")
        vote = Vote(game_order=game_order)
        vote.save()
        return redirect('poller')
    
    games = Game.objects.all()
    return render(request, 'poller/poller.html', {'games': games})

def results_view(request):
    votes = Vote.objects.all()
    games = Game.objects.all()
    game_dict = {str(game.id): game.name for game in games}
    
    for vote in votes:
        vote.game_names = [game_dict[game_id] for game_id in vote.game_order]
    
    # Borda count algorithm
    game_points = {game.id: 0 for game in games}
    for vote in votes:
        for index, game_id in enumerate(vote.game_order):
            game_points[int(game_id)] += len(games) - index
    
    sorted_games = sorted(game_points.items(), key=lambda item: item[1], reverse=True)
    winner_order = [game_dict[str(game_id)] for game_id, points in sorted_games]
    
    return render(request, 'results.html', {'votes': votes, 'winner_order': winner_order})

def index_view(request):
    return render(request, 'index.html')
