from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .models import Candidate, PdfMenschen_A1, AudioMenschen_A1, PdfMenschen_A2, AudioMenschen_A2, PdfMenschen_B1, \
    AudioMenschen_B1, PdfGrammatik_Aktiv, AudioGrammatik_Aktiv, Transcript
from django.contrib.auth.models import User
from .forms import DocumentUploadForm


@login_required(login_url='/login/')
def download_view(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    return render(request, 'downloads.html', {
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_a1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_A1.objects.all()
    audio_resources = AudioMenschen_A1.objects.all()

    return render(request, 'Menschen_A1.html', {
        'pdf_resources': pdf_resources,
        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_a2(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_A2.objects.all()
    audio_resources = AudioMenschen_A2.objects.all()

    return render(request, 'Menschen_A2.html', {
        'pdf_resources': pdf_resources,
        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def menschen_b1(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfMenschen_B1.objects.all()
    audio_resources = AudioMenschen_B1.objects.all()

    return render(request, 'Menschen_b1.html', {
        'pdf_resources': pdf_resources,
        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def Grammatik_Aktiv(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate

    pdf_resources = PdfGrammatik_Aktiv.objects.all()
    audio_resources = AudioGrammatik_Aktiv.objects.all()

    return render(request, 'Grammatik_Aktiv.html', {
        'pdf_resources': pdf_resources,
        'audio_resources': audio_resources,
        'candidate': candidate
    })


@login_required(login_url='/login/')
def home(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate
    context = {'candidate': candidate}
    return render(request, 'home.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.filter(email=email).first()
            if user:
                user = authenticate(request, username=user.username, password=password)
                if user is not None:
                    login(request, user)
                    candidate = getattr(user, 'candidate', None)
                    if candidate and candidate.needs_password_change:
                        return redirect('change_password_url')
                    return redirect('/')
                else:
                    messages.error(request, 'Email or password is not correct')
            else:
                messages.error(request, 'Account does not exist.')
        return render(request, 'login.html')


from django.contrib.auth import update_session_auth_hash


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            user.candidate.needs_password_change = False
            user.candidate.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='/login/')
def coursework(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate
    context = {'candidate': candidate}
    return render(request, 'coursework.html', context)


@login_required(login_url='/login/')
def attendance(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate
    context = {'candidate': candidate}
    return render(request, 'Attendance.html', context)


@login_required(login_url='/login/')
def payments(request):
    candidate = None
    if hasattr(request.user, 'candidate'):
        candidate = request.user.candidate
    context = {'candidate': candidate}
    return render(request, 'payments.html', context)


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                user = form.save()  # This saves the User instance and returns it
            messages.success(request, f'Account was created for {user.username}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@login_required(login_url='/login/')
def upload_documents(request):
    candidate, created = Candidate.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = DocumentUploadForm(request.POST, request.FILES, instance=candidate)
        if form.is_valid():
            # Handle related objects, e.g., transcripts
            transcripts = request.FILES.getlist('transcripts')
            for transcript_file in transcripts:
                Transcript.objects.create(candidate=candidate, other_transcripts=transcript_file)

            form.save()
            messages.success(request, 'Your documents have been updated successfully.')
            return redirect('upload_documents')
    else:
        form = DocumentUploadForm(instance=candidate)

    # Fetch the transcripts related to the candidate
    transcripts = candidate.transcripts.all()

    context = {
        'form': form,
        'candidate': candidate,
        'transcripts': transcripts
    }
    return render(request, 'upload_documents.html', context)


@login_required(login_url='/login/')
def delete_transcript(request, transcript_id):
    transcript = get_object_or_404(Transcript, id=transcript_id, candidate__user=request.user)
    transcript.delete()
    messages.success(request, "Transcript deleted successfully.")
    return redirect('upload_documents')  # Replace 'upload_documents' with the name of your view that displays the form


def delete_document(request, doc_type):
    candidate = get_object_or_404(Candidate, user=request.user)
    try:
        if doc_type == 'birth_certificate':
            candidate.Birth_certificate.delete()
        elif doc_type == 'photo':
            candidate.photo.delete()
        elif doc_type == 'good_conduct':
            candidate.certificate_of_good_conduct.delete()
        elif doc_type == 'licence':
            candidate.Licence_file.delete()
        elif doc_type == 'high_school':
            candidate.High_School_file.delete()
        elif doc_type == 'university':
            candidate.University_file.delete()
        elif doc_type == 'resume':
            candidate.resume_file.delete()
        elif doc_type == 'id_card':
            candidate.identification_card_file.delete()
        candidate.save()
        messages.success(request, 'Document has been deleted successfully.')
    except Exception as e:
        messages.error(request, 'An error occurred when trying to delete the document.')
    return redirect('upload_documents')

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.management import call_command
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def import_candidates_view(request):
    if request.method == "POST":
        call_command('import_candidates')
        # Redirect to a new URL or return a success message
        return HttpResponseRedirect(reverse('your-success-view'))
    else:
        return HttpResponseRedirect(reverse('your-fallback-view'))
