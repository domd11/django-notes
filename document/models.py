from pyexpat import model
from django.db import models

# Create your models here.


class Document(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=25)
    priority = models.CharField(max_length=7)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('title',)
