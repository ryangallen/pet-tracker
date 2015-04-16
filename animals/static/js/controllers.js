var petTrackerControllers = angular.module('petTrackerControllers', []);

petTrackerControllers.controller('PetTrackerController', [
    '$scope',
    '$q',
    'PetTrackerFactory',
    function($scope, $q, PetTrackerFactory){
        $scope.ordering = "id";
        $scope.order = function(prop){
            $scope.ordering = $scope.ordering == prop ? "-" + prop : prop
        }

        $scope.filterAnimal = function(pet){
            return pet.breed.animal.showing;
        }

        var animalsPromise = PetTrackerFactory.readAnimals().then(
            function(promise){$scope.animals = promise.data.results}
        );
        var breedsPromise = PetTrackerFactory.readBreeds().then(
            function(promise){$scope.breeds = promise.data.results}
        );
        var petsPromise = PetTrackerFactory.readPets().then(
            function(promise){$scope.pets = promise.data.results}
        );

        $q.all([animalsPromise, breedsPromise, petsPromise]).then(function(){
            _.each($scope.animals, function(animal){
                animal.showing = true;
                var animalBreeds = _.where($scope.breeds, {animal: animal.id});
                _.each(animalBreeds, function(breed){
                    breed.animal = animal;
                    var breedPets = _.where($scope.pets, {breed: breed.id});
                    _.each(breedPets, function(pet){
                        pet.breed = breed;
                    });
                });
            });
        });
    }
]);
