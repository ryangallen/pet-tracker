from django.db import models


class Animal(models.Model):
    name = models.CharField(max_length=60, unique=True)
    scientific_name = models.CharField(max_length=60, null=True,
                                       blank=True, unique=True)

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=50)
    animal = models.ForeignKey('Animal')

    def __str__(self):
        return self.name

    class Meta:
        unique_together = (('name', 'animal'),)


class Pet(models.Model):
    name = models.CharField(max_length=30)
    breed = models.ForeignKey('Breed')
    birthday = models.DateField()

    def __str__(self):
        return self.name
