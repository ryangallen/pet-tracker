from datetime import date

from django.core.exceptions import ValidationError
from django.test import TestCase

from animals.models import Animal, Breed, Pet


class AnimalModelTest(TestCase):
    fixtures = ['animals.json',]

    def test_animal_string(self):
        animal_name = "Dog"
        animal = Animal.objects.get(name=animal_name)
        self.assertEqual(str(animal), animal_name)

    def test_breed_string(self):
        breed_name = "German Shepherd"
        breed = Breed.objects.get(name=breed_name)
        self.assertEqual(str(breed), breed_name)

    def test_pet_string(self):
        pet_name = "Fido"
        pet = Pet.objects.get(name=pet_name)
        self.assertEqual(str(pet), pet_name)

    def test_breed_name_max_length(self):
        char50 = "a" * 50
        animal = Animal.objects.first()
        Breed.objects.create(name=char50, animal=animal)

        breed = Breed.objects.create(name=(char50 + "a"), animal=animal)
        self.assertRaises(ValidationError, breed.full_clean)

    def test_pet_name_max_length(self):
        char30 = "a" * 30
        breed = Breed.objects.first()
        birthday = date.today()
        Pet.objects.create(name=char30, breed=breed, birthday=birthday)

        pet = Pet.objects.create(name=(char30 + "a"), breed=breed,
                                 birthday=birthday)
        self.assertRaises(ValidationError, pet.full_clean)
