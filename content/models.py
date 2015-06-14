from django.db import models

base_races = ["Elf", "Dwarf", "Gnome", "Half-Elf",
              "Halfling", "Half-Orc", "Human"]

base_race_choices = [(race, race) for race in base_races]
class Race(models.Model):
    name = models.CharField(max_length=255, choices=base_race_choices)
    size = models.CharField(max_length=255)
    base_speed = models.IntegerField()
    description = models.TextField()
    history = models.TextField()

# class RacialTrait(models.Model):
#
# class RacialFeat(models.Model):
#
# class AbiilityModifier(models.Model):
