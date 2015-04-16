from rest_framework import serializers

from animals.models import Animal, Breed, Pet


class AnimalSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Animal
        fields = ('id', 'name', 'scientific_name',)


class BreedSerializer(serializers.HyperlinkedModelSerializer):
    animal = serializers.PrimaryKeyRelatedField(queryset=Animal.objects.all())

    class Meta:
        model = Breed
        fields = ('id', 'name', 'animal',)


class PetSerializer(serializers.HyperlinkedModelSerializer):
    breed = serializers.PrimaryKeyRelatedField(queryset=Breed.objects.all())

    class Meta:
        model = Pet
        fields = ('id', 'name', 'breed', 'birthday',)
