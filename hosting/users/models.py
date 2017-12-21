from django.db import models
from django.utils import timezone

class roles(models.Model):
    rol_id = models.IntegerField()
    description = models.CharField(max_length=200)

class Users(models.Model):
    user = models.CharField(max_length=20)
    pg_password = models.CharField(max_length=50)
    ftp_password = models.CharField(max_length=50)
    rol_id = models.ForeignKey(roles, on_delete=models.CASCADE)
    fecha_alta = models.DateTimeField(default=timezone.now)