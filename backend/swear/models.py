from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Swear(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    bjorn = models.IntegerField(default=0)
    alex = models.IntegerField(default=0)
    wang = models.IntegerField(default=0)
    patrick = models.IntegerField(default=0)
    dario = models.IntegerField(default=0)
    davide = models.IntegerField(default=0)
    rafael = models.IntegerField(default=0)