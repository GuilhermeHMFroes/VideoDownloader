from django.db import models


# Create your models here.
class DownloadedVideos(models.Model):
    criado_em = models.DateTimeField(auto_now_add=True, blank=True)
    thumbnail = models.CharField(max_length=512)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    views = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    formato = models.CharField(max_length=255)
    
    def __str__(self):
            return self.title
