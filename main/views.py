from django.shortcuts import render
from .models import Player
from .forms import PlayerForm
from django.utils.crypto import get_random_string
import django_tables2 as tables
from .tables import PlayerTable

def join(request):
    form = PlayerForm(request.POST or None)
    username = ""
    url = ""
    flag = ""
    
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        if form.is_valid():
            flag = get_random_string(length=16)
            player = form.save(commit=False)
            player.flag = flag
            username = player.username
            url = player.url
            player.save()

    return render(request, 'main/join.html',
    context={
        'form': form,
        'flag': flag,
        'username': username,
        'url': url
    })

def board(request):
    players_done = Player.objects.filter(complete=True)
    table_done = PlayerTable(players_done)
    players_not = Player.objects.filter(complete=False)
    table_not = PlayerTable(players_not)
    return render(request, 'main/board.html',
    context={
        'table_done': table_done,
        'table_not': table_not
    })