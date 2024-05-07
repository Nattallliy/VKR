from django.db import models

class Peoples(models.Model):
    FIO = models.CharField(max_length=128)
    birthday = models.DateField()


