from django.contrib import admin
from .models import (AudioMenschen_A1, AudioMenschen_A2, AudioMenschen_B1, AudioGrammatik_Aktiv, )
from import_export.admin import ImportExportModelAdmin



@admin.register(AudioMenschen_A1)
class AudioMenschen_A1Admin(ImportExportModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


@admin.register(AudioMenschen_A2)
class AudioMenschen_A2Admin(ImportExportModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


@admin.register(AudioMenschen_B1)
class AudioMenschen_B1Admin(ImportExportModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)


@admin.register(AudioGrammatik_Aktiv)
class AudioGrammatik_AktivAdmin(ImportExportModelAdmin):
    list_display = ('title', 'audio_file')
    list_filter = ('title',)
