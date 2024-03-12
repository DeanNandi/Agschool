from django.db import models


class AudioMenschen_A1(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title


class AudioMenschen_A2(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title


class AudioMenschen_B1(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title


class AudioGrammatik_Aktiv(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audio/')

    def __str__(self):
        return self.title
