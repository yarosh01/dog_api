from django.db import models
from django.utils.translation import gettext_lazy as _


class Breed(models.Model):

    class Size(models.TextChoices):
        Tiny = 'TN', _('Tiny')
        Small = 'SM', _('Small')
        Medium = 'MD', _('Medium')
        Large = 'LR', _('Large')

    class Train(models.IntegerChoices):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100, choices=Size.choices, default=Size.Medium)
    friendliness = models.IntegerField(choices=Train.choices)
    trainability = models.IntegerField(choices=Train.choices)
    sheddingamount = models.IntegerField(choices=Train.choices)
    exerciseneeds = models.IntegerField(choices=Train.choices)

    def __str__(self):
        return self.name


class Dog(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    favoritefood = models.CharField(max_length=100)
    favoritetoy = models.CharField(max_length=100)

    def __str__(self):
        return self.name
