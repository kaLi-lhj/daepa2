from django.db import models

# Create your models here.
class Error(models.Model):
    code = models.CharField(max_length=10)
    code_name = models.CharField(max_length=50, blank=True)
    note = models.CharField(max_length=255)