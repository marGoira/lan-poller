from django.shortcuts import render, redirect
from .models import Game, Vote
from .forms import VoteForm

def poller_view(request):
    games = Game.objects.all()
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.votes += 1
            vote.save()
            return redirect('poller')
    else:
        form = VoteForm()
    return render(request, 'poller/poller.html', {'form': form, 'games': games})

def index_view(request):
    return render(request, 'index.html')