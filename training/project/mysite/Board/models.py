from django.db import models
from django.contrib.auth.models import User
import os

# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file_upload = models.FileField(upload_to='board/data/%Y/%m/%d', blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return '[PK : {}]-{} :: {}'.format(self.pk, self.title, self.author)
    
    def get_FileName(self):
        return os.path.basename(self.file_upload.name)
    
    def get_absolute_url(self):
        return '/Board/{}'.format(self.pk)
    