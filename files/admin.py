from django.contrib import admin
from .models import (PdfMenschen_A1, PdfMenschen_A2, PdfMenschen_B1,PdfGrammatik_Aktiv, )
from import_export.admin import ImportExportModelAdmin



@admin.register(PdfMenschen_A1)
class PdfMenschen_A1Admin(ImportExportModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(PdfMenschen_A2)
class PdfMenschen_A2Admin(ImportExportModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(PdfMenschen_B1)
class PdfMenschen_B1Admin(ImportExportModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)


@admin.register(PdfGrammatik_Aktiv)
class PdfGrammatik_AktivAdmin(ImportExportModelAdmin):
    list_display = ('title', 'pdf_file')
    list_filter = ('title',)
