from django.db import models

class Core(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    back_story = models.TextField()
    height = models.CharField(max_length=50)
    weight = models.FloatField()
    strength = models.IntegerField()
    wisdom = models.IntegerField()
    constitution = models.IntegerField()
    dexterity = models.IntegerField()
    intelligence = models.IntegerField()
    charisma = models.IntegerField()
