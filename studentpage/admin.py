from django.contrib import admin
from .models import (
    Candidate, PdfMenschen_A1, AudioMenschen_A1,
    PdfMenschen_A2, AudioMenschen_A2,
    PdfMenschen_B1, AudioMenschen_B1,
    PdfGrammatik_Aktiv, AudioGrammatik_Aktiv,
    Transcript
)
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.contrib import admin
from .models import CandidateToken

@admin.register(CandidateToken)
class CandidateTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token', 'get_email')
    search_fields = ('user__username', 'user__email', 'token')
    # readonly_fields = ('token',)  # Make 'token' read-only if you prefer tokens to be auto-generated or immutable

    def get_email(self, obj):
        return obj.user.email
    get_email.admin_order_field = 'user__email'  # Allows column order sorting
    get_email.short_description = 'Email'  # Column header





class TranscriptInline(admin.TabularInline):
    model = Transcript
    extra = 1  # Number of empty forms to display




@admin.register(Transcript)
class TranscriptAdmin(admin.ModelAdmin):
    list_display = ('candidate', 'file_link')
    list_filter = ('candidate',)

    def file_link(self, obj):
        if obj.other_transcripts:  # Changed from 'file' to 'other_transcripts'
            return format_html(f'<a href="{obj.other_transcripts.url}" target="_blank">View File</a>')
        return "No file uploaded"

    file_link.short_description = 'Transcript File'


# Admin for PDF and Audio Resources for Menschen A1
@admin.register(PdfMenschen_A1)
class PdfMenschen_A1Admin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(AudioMenschen_A1)
class AudioMenschen_A1Admin(admin.ModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)



# Admin for PDF and Audio Resources for Menschen A2
@admin.register(PdfMenschen_A2)
class PdfMenschen_A2Admin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(AudioMenschen_A2)
class AudioMenschen_A2Admin(admin.ModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


# Admin for PDF and Audio Resources for Menschen B1
@admin.register(PdfMenschen_B1)
class PdfMenschen_B1Admin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(AudioMenschen_B1)
class AudioMenschen_B1Admin(admin.ModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


# Admin for PDF and Audio Resources for Menschen B2
@admin.register(PdfGrammatik_Aktiv)
class PdfGrammatik_AktivAdmin(admin.ModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(AudioGrammatik_Aktiv)
class AudioGrammatik_AktivAdmin(admin.ModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


from django.contrib import admin
from django.core.management import call_command
from .models import Candidate
from django.http import HttpResponseRedirect
from django.urls import reverse


def import_candidates(modeladmin, request, queryset):
    # Assuming the path to your JSON file is static; adjust as needed
    json_file_path = 'C:\\Users\\Dell\\PycharmProjects\\Agcrm\\candidates_export.json'

    try:
        # Call your custom command directly
        call_command('import_updated_candidates', json_file_path)
        modeladmin.message_user(request, "Candidates imported successfully.")
    except Exception as e:
        modeladmin.message_user(request, f"Error importing candidates: {e}")


import_candidates.short_description = "Import Candidates from AGCRM"

# Existing CandidateAdmin class
@admin.register(Candidate)
class CandidateAdmin(ImportExportModelAdmin):
    actions = [import_candidates]
    list_display = ('First_Name', 'Last_Name', 'admission_number', 'email_address')
    list_filter = ('First_Name', 'Last_Name', 'admission_number', 'email_address')
    list_per_page = 15

    # Add the inline for Transcripts
    inlines = [TranscriptInline]


