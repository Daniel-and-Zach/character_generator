from django.db import models

class Core(models.Model):
    name = models.CharField(max_length=100)
    race = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    backstory = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    strength = models.CharField(max_length=100)
    wisdom = models.CharField(max_length=100)
    constitution = models.CharField(max_length=100)
    dexterity = models.CharField(max_length=100)
    intelligence = models.CharField(max_length=100)
    charisma = models.CharField(max_length=100)
