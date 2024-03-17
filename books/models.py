from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=500, blank=True, null=True)
    author = models.CharField(max_length=500, blank=True, null=True)
    media_type = models.CharField(max_length=500, blank=True, null=True)
    gutenberg_id=models.BigIntegerField(blank=True, null=True)
    download_count = models.CharField(max_length=100,blank=True, null=True)
    bookshelf_name = models.CharField(max_length=500, blank=True, null=True)
    mime_type = models.CharField(max_length=500,blank=True, null=True)
    url = models.CharField(max_length=500,blank=True, null=True)
    language= models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return str(self.pk)


