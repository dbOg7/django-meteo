from sys import maxsize
from django.db import models

# Create your models here.
class CitiesModel(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return  str(self.name)