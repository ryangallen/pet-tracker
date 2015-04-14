from rest_framework import viewsets

from animals.models import Animal, Breed, Pet
from animals.api.serializers import (AnimalSerializer,
                                     BreedSerializer,
                                     PetSerializer)


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class PetViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
