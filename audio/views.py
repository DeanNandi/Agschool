from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import AudioMenschen_A1, AudioMenschen_B1, AudioGrammatik_Aktiv, AudioMenschen_A2


@login_required(login_url='/login/')
def menschen_a1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    audio_resources = AudioMenschen_A1.objects.all()

    return render(request, 'audio/Menschen_A1.html', {

        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_a2(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    audio_resources = AudioMenschen_A2.objects.all()

    return render(request, 'audio/Menschen_A2.html', {

        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_b1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    audio_resources = AudioMenschen_B1.objects.all()

    return render(request, 'audio/Menschen_b1.html', {
        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def Grammatik_Aktiv(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    audio_resources = AudioGrammatik_Aktiv.objects.all()

    return render(request, 'audio/Grammatik_Aktiv.html', {

        'audio_resources': audio_resources,
        'candidate': candidate
    })
