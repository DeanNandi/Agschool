from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import PdfMenschen_A1, PdfMenschen_A2, PdfMenschen_B1, PdfGrammatik_Aktiv


@login_required(login_url='/login/')
def menschen_a1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_A1.objects.all()

    return render(request, 'files/Menschen_A1.html', {
        'pdf_resources': pdf_resources,

        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_a2(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_A2.objects.all()

    return render(request, 'files/Menschen_A2.html', {
        'pdf_resources': pdf_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_b1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_B1.objects.all()

    return render(request, 'files/Menschen_b1.html', {
        'pdf_resources': pdf_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def Grammatik_Aktiv(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfGrammatik_Aktiv.objects.all()

    return render(request, 'files/Grammatik_Aktiv.html', {
        'pdf_resources': pdf_resources,
        'candidate': candidate
    })
