from django.shortcuts import render, redirect, get_object_or_404
from .forms import VoleyPlayerForm
from .models import VoleyPlayer


def player_list(request):
    players = VoleyPlayer.objects.all()
    return render(request, 'player_list.html', {'players': players})


def add_player(request):
    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = VoleyPlayerForm()

    return render(request, 'add_player.html', {'form': form})


def update_player(request, id):
    player = get_object_or_404(VoleyPlayer, id=id)

    if request.method == 'POST':
        form = VoleyPlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = VoleyPlayerForm(instance=player)

    return render(request, 'update_player.html', {'form': form, 'player': player})


def delete_player(request, id):
    player = get_object_or_404(VoleyPlayer, id=id)

    if request.method == 'POST':
        player.delete()
        return redirect('player_list')

    return render(request, 'delete_player.html', {'player': player})