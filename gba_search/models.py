from django.db import models

class Person(models.Model):
    dni = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    lastname = models.CharField(max_length=100, blank=False, null=False)
    birth_day = models.DateField(blank=False, null=False)
    is_gba = models.BooleanField(default=False)
