from django.db import models

class Race(models.Model):
    name = models.CharField(max_length=255, choices=base_races)
    size = models.CharField(max_length=255)
    base_speed = models.IntegerField()
    description = models.TextField()
    history = models.TextField()

base_races = ["Elf", "Dwarf", "Gnome", "Half-Elf",
              "Halfling", "Half-Orc", "Human"]

# class RacialTrait(models.Model):
#
# class RacialFeat(models.Model):
#
# class AbiilityModifier(models.Model):
