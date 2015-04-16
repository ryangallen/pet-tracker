var petTrackerDirectives = angular.module('petTrackerDirectives', [])

petTrackerDirectives
    .directive('petList', [
        '$q',
        'PetTrackerFactory',
        function($q, PetTrackerFactory){
            return {
                restrict: 'E',
                templateUrl: "/static/js/templates/pet_list.html",
                replace: true,
                link: function(scope){
                    scope.ordering = "id";
                    scope.order = function(prop){
                        scope.ordering = scope.ordering == prop ? "-" + prop : prop
                    }

                    scope.filterAnimal = function(pet){
                        return pet.breed.animal.showing;
                    }

                    var animalsPromise = PetTrackerFactory.readAnimals().then(
                        function(promise){scope.animals = promise.data.results}
                    );
                    var breedsPromise = PetTrackerFactory.readBreeds().then(
                        function(promise){scope.breeds = promise.data.results}
                    );
                    var petsPromise = PetTrackerFactory.readPets().then(
                        function(promise){scope.pets = promise.data.results}
                    );

                    $q.all([animalsPromise, breedsPromise, petsPromise]).then(function(){
                        _.each(scope.animals, function(animal){
                            animal.showing = true;
                            var animalBreeds = _.where(scope.breeds, {animal: animal.id});
                            _.each(animalBreeds, function(breed){
                                breed.animal = animal;
                                var breedPets = _.where(scope.pets, {breed: breed.id});
                                _.each(breedPets, function(pet){
                                    pet.breed = breed;
                                });
                            });
                        });
                    });

                    scope.showPetDetails = function(pet){
                        scope.focusedPet = pet;
                    }
                }
            }
        }
    ])
    .directive('petDetails', ['PetTrackerFactory',
        function(PetTrackerFactory){
            return {
                restrict: 'E',
                templateUrl: "/static/js/templates/pet_details.html",
                replace: true,
                scope: {
                    pets: '=',
                    pet: '=',
                },
                link: function(scope){
                    scope.verifyDelete = function(){
                        scope.deletingPet = true;
                    }
                    scope.cancelDelete = function(){
                        scope.deletingPet = false;
                        scope.deleteVerification = null;
                    }
                    scope.deletePet = function(){
                        var removeObject = function(list, properties){
                            if (!list) return;
                            var objectIndex = _.indexOf(list, _.findWhere(list, properties));
                            list.splice(objectIndex, 1);
                        }

                        PetTrackerFactory.deletePet(scope.pet.id).then(
                            function(promise){
                                removeObject(scope.pets, {id: scope.pet.id})
                                scope.cancelDelete();
                                scope.pet = null;
                            }
                        );
                    }
                }
            }
        }
    ]);
