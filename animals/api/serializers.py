from rest_framework import serializers

from animals.models import Animal, Breed, Pet


class AnimalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Animal
        fields = ('name', 'scientific_name',)


class BreedSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Breed
        fields = ('name', 'animal',)


class PetSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pet
        fields = ('name', 'breed', 'birthday',)
