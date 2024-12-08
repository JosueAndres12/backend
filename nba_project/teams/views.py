from django.shortcuts import render
from .models import Team
from django.http import HttpResponseRedirect
from .forms import TeamForm
from django.core.mail import send_mail

def team_list(request):
    query = request.GET.get('q', '')
    if query:
        teams = Team.objects.filter(name__icontains=query)
    else:
        teams = Team.objects.all()
    return render(request, 'teams/team_list.html', {'teams': teams, 'query': query})

def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TeamForm()
    return render(request, 'teams/add_team.html', {'form': form})

def send_email_notification(request):
    send_mail(
        'Nuevo Equipo Añadido',
        'Se ha añadido un nuevo equipo a la base de datos.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect('/')